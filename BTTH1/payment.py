from base_employee import BaseEmployee

class VietcombankCorporateService:
    def transfer_salary(self, employee: BaseEmployee, amount: float):
        print(f"[Hệ thống VCB Corporate]: Đang kết nối tới cổng chi trả Rikkei...")
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Ngân hàng đối tác (VCB) đã giải ngân thành công số tiền: {amount:,.0f} VND tới nhân sự {employee.emp_code}.")

class TechcombankCorporateService:
    def transfer_salary(self, employee: BaseEmployee, amount: float):
        print(f"[Hệ thống TCB Corporate]: Đang kết nối tới cổng chi trả Rikkei...")
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Ngân hàng đối tác (TCB) đã giải ngân thành công số tiền: {amount:,.0f} VND tới nhân sự {employee.emp_code}.")

def execute_payroll(payment_service, employee: BaseEmployee, amount: float):
    try:
        payment_service.transfer_salary(employee, amount)
    except AttributeError:
        print("LỖI: Cổng dịch vụ ngân hàng doanh nghiệp không hợp lệ hoặc chưa được liên kết liên thông kỹ thuật.")