from base_employee import BaseEmployee

class Lecturer(BaseEmployee):
    def __init__(self, emp_code: str, full_name: str, teaching_slots: int = 0):
        super().__init__(emp_code, full_name)
        self.teaching_slots = teaching_slots

    def calculate_salary(self) -> float:
        return (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000)

    def update_kpi(self, progress: float):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        print(f"Tiến độ giảng dạy và đánh giá KPI cập nhật: {progress}%")

    def conduct_class(self):
        self.teaching_slots += 1
        self._add_working_hours(2.0)

class AdmissionStaff(BaseEmployee):
    def __init__(self, emp_code: str, full_name: str, kpi_target: float):
        super().__init__(emp_code, full_name)
        self.revenue_generated = 0.0
        self.kpi_target = kpi_target

    def calculate_salary(self) -> float:
        return (self.working_hours * self.base_salary_rate) + (self.revenue_generated * 0.05)

    def update_kpi(self, new_revenue: float):
        if new_revenue <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        self.revenue_generated += new_revenue

class HybridManager(Lecturer, AdmissionStaff):
    def __init__(self, emp_code: str, full_name: str, kpi_target: float):
        BaseEmployee.__init__(self, emp_code, full_name)
        self.teaching_slots = 0
        self.revenue_generated = 0.0
        self.kpi_target = kpi_target

    def calculate_salary(self) -> float:
        salary_base = self.working_hours * self.base_salary_rate
        bonus_teaching = self.teaching_slots * 500000
        bonus_revenue = self.revenue_generated * 0.05
        return salary_base + bonus_teaching + bonus_revenue

    def update_kpi(self, progress_or_revenue: float, is_revenue: bool = False):
        if is_revenue:
            AdmissionStaff.update_kpi(self, progress_or_revenue)
        else:
            Lecturer.update_kpi(self, progress_or_revenue)