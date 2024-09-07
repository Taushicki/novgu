from database.requests import DataBaseRequests

from api.services.pdf import PDF
import pymorphy2
import inspect
from collections import namedtuple

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


def change_morphy(string: str):
    morph = pymorphy2.MorphAnalyzer()
    name = ""
    for i in string.split(" "):
        name += morph.parse(i)[0].inflect({"gent"}).word + " "
    return name[:-1]


class UTILS:
    @staticmethod
    async def get_student_by_manid(manid: int):
        try:
            return await DataBaseRequests.get_student_by_manid(manid=manid)
        except Exception as error:
            raise error

    @staticmethod
    async def get_subjects_by_manid(manid: int):
        try:
            return await DataBaseRequests.get_subjects_by_manid(manid=manid)
        except Exception as error:
            raise error

    @staticmethod
    def create_pdf(student_data, student_subjects, output_file_name):

        subjects = []
        debt = []
        for subject in student_subjects:
            subjects.append(
                (
                    str(subject["semestr"]),
                    subject["subject"],
                    subject["att_form"],
                    subject["rating18"].split()[0],
                    subject["week18"],
                )
            )
        last_semest = subjects[-1][0]
        for subject in subjects:
            if subject[0] == last_semest and int(subject[4]) <= 2:
                debt.append(subject[1])
        PDF().create_certificate(
            output_file_name,
            student_data["COURCE"],
            student_data["GRP_NAME"],
            change_morphy(student_data["FS_NAME"]),
            f"{change_morphy(student_data['SURNAME'])} {change_morphy(student_data['NAME'])} {change_morphy(student_data['PATRON'])}",
            f"{student_data['SURNAME']} {student_data['NAME']} {student_data['PATRON']}",
            f"{student_data['SPE_SHIFR']} {student_data['SPEC_NAME']}",
            subjects,
            debt,
        )
