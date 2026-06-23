from abc import ABC, abstractmethod

class BaseEmployee(ABC):
    company_name = "Rikkei Education"
    base_salary_rate = 3000000

    def __init__(self, emp_code: str, full_name: str):
        if not self.validate_employee_code(emp_code):
            raise ValueError("Mã nhân sự không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng RKE.")
        
        self.emp_code = emp_code
        self.full_name = " ".join(full_name.split()).upper()
        self.__working_hours = 0.0

    @property
    def working_hours(self):
        return self.__working_hours

    def _add_working_hours(self, hours: float):
        if hours <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        self.__working_hours += hours

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    @abstractmethod
    def update_kpi(self, progress: float):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours + other.working_hours

    def __lt__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours < other.working_hours

    @staticmethod
    def validate_employee_code(emp_code: str) -> bool:
        return isinstance(emp_code, str) and len(emp_code) == 10 and emp_code.startswith("RKE")

    @classmethod
    def update_base_salary_rate(cls, new_rate: float):
        if new_rate <= 0:
            raise ValueError("Mức lương cơ sở phải lớn hơn 0.")
        cls.base_salary_rate = new_rate
        