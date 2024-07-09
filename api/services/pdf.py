import io
import pymorphy2
import inspect
from collections import namedtuple
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from api.dto.student_dto import Student
from datetime import datetime


ArgSpec = namedtuple("ArgSpec", "args varargs keywords defaults")


def patched_getargspec(func):
    spec = inspect.getfullargspec(func)
    return ArgSpec(
        args=spec.args,
        varargs=spec.varargs,
        keywords=spec.varkw,
        defaults=spec.defaults,
    )


inspect.getargspec = patched_getargspec


class PDF:
    async def create(self, student: Student, output_file_name):
        self.replace_words_in_pdf(
            "base.pdf",
            datetime.now().date().strftime("%d.%m.%Y"),
            student,
            "На данный момент академических задолжностей не имеет.",
            output_file_name,
        )

    def split_into_lines(self, text: str, max_length: int = 70) -> list[str]:
        if not text:
            return []

        lines = []
        current_line = ""

        for word in text.split():
            if len(current_line) + len(word) + 1 <= max_length:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        if current_line:
            lines.append(current_line.strip())

        return lines

    def replace_words_in_pdf(
        self, file_path: str, date: str, student: Student, result: str, output_file_name,
    ) -> None:
        existing_pdf = open(file_path, "rb")
        pdf_reader = PdfReader(existing_pdf)
        output = PdfWriter()

        new_pdf = open(output_file_name, "wb")

        page = pdf_reader.pages[0]

        packet = io.BytesIO()
        can = canvas.Canvas(packet)

        pdfmetrics.registerFont(TTFont("TimesNewRoman", "times.ttf"))

        can.setFont("TimesNewRoman", 14)

        rows = self.split_into_lines(
            f"Новгородский государственный университет имени Ярослава Мудрого предоставляет сведения об успеваемости на {date}, студента {student.courсe} курса группы {student.group} {self.change_morphy(student.form)} формы обучения {self.change_morphy(student.name).title()} по специальности {student.spec}."
        )
        can.drawString(120, 513, rows[0])
        y = 497
        for row in rows[1:]:
            can.drawString(85, y, row)
            y -= 16
        can.drawString(120, y, result)
        can.save()

        packet.seek(0)
        new_pdf_page = PdfReader(packet).pages[0]
        page.merge_page(new_pdf_page)

        output.add_page(page)
        output.write(new_pdf)

        existing_pdf.close()
        new_pdf.close()

    def change_morphy(self, string: str):
        morph = pymorphy2.MorphAnalyzer()
        name = ""
        for i in string.split(" "):
            name += morph.parse(i)[0].inflect({"gent"}).word + " "
        return name[:-1]
