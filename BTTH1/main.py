from roles import Lecturer, AdmissionStaff, HybridManager
from payment import VietcombankCorporateService, TechcombankCorporateService, execute_payroll

def main():
    employees = []
    current_employee = None

    while True:
        print("\n===== RIKKEI EDUCATION HR SIMULATOR PRO =====")
        print("1. Tuyển dụng nhân sự mới")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Ghi nhận công nhật & Cập nhật KPI")
        print("4. Tổng hợp quỹ lương và ngân sách chi trả")
        print("5. Kiểm tra gộp giờ làm việc & So sánh hiệu suất")
        print("6. Giải ngân lương qua Cổng thanh toán đối tác")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ")

        if choice == '1':
            print("--- CHỌN LOẠI NHÂN SỰ KHỞI TẠO ---")
            print("1. Lecturer (Giảng viên chuyên trách)")
            print("2. Admission Staff (Nhân viên Tuyển sinh)")
            print("3. Hybrid Manager (Quản lý kiêm Giảng dạy)")
            type_choice = input("Chọn loại nhân sự (1-3): ")
            
            emp_code = input("Nhập mã nhân sự 10 ký tự: ")
            full_name = input("Nhập họ và tên: ")

            try:
                if type_choice == '1':
                    emp = Lecturer(emp_code, full_name)
                    print(f"Tuyển dụng Giảng viên thành công! Tên nhân sự: {emp.full_name}")
                elif type_choice == '2':
                    target = float(input("Nhập chỉ tiêu KPI doanh số: "))
                    emp = AdmissionStaff(emp_code, full_name, target)
                    print(f"Tuyển dụng NV Tuyển sinh thành công! Tên nhân sự: {emp.full_name}")
                elif type_choice == '3':
                    target = float(input("Nhập chỉ tiêu KPI doanh số: "))
                    emp = HybridManager(emp_code, full_name, target)
                    print(f"Tuyển dụng Hybrid Manager thành công! Tên nhân sự: {emp.full_name}")
                else:
                    print("Lựa chọn không hợp lệ.")
                    continue
                
                employees.append(emp)
                current_employee = emp
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(f"Lỗi khởi tạo (TypeError): {e}")

        elif choice == '2':
            if not current_employee:
                print("Chưa có nhân sự nào được chọn.")
                continue
            
            print("\n--- THÔNG TIN NHÂN SỰ HIỆN TẠI ---")
            print(f"Loại nhân sự: {current_employee.__class__.__name__}")
            print(f"Mã nhân sự: {current_employee.emp_code}")
            print(f"Họ và tên: {current_employee.full_name}")
            print(f"Số giờ làm việc: {current_employee.working_hours} giờ")
            
            if hasattr(current_employee, 'teaching_slots'):
                print(f"Số ca đã dạy: {current_employee.teaching_slots} ca")
            if hasattr(current_employee, 'revenue_generated'):
                print(f"Doanh số mang về: {current_employee.revenue_generated:,.0f} VND")
            
            print("\n[MRO]:", [cls.__name__ for cls in current_employee.__class__.mro()])

        elif choice == '3':
            if not current_employee:
                print("Chưa có nhân sự nào được chọn.")
                continue

            print("\n--- GHI NHẬN CÔNG NHẬT & HIỆU SUẤT ---")
            print("1. Ghi nhận tham gia đứng lớp")
            print("2. Cập nhật tiến độ KPI / Doanh số")
            task_choice = input("Chọn tác vụ (1-2): ")

            try:
                if task_choice == '1':
                    if hasattr(current_employee, 'conduct_class'):
                        current_employee.conduct_class()
                        print("Ghi nhận thành công!")
                    else:
                        print("Nhân sự này không có chức năng đứng lớp.")
                elif task_choice == '2':
                    if isinstance(current_employee, HybridManager):
                        val = float(input("Nhập giá trị doanh số: "))
                        current_employee.update_kpi(val, is_revenue=True)
                    elif isinstance(current_employee, AdmissionStaff):
                        val = float(input("Nhập giá trị doanh số: "))
                        current_employee.update_kpi(val)
                    elif isinstance(current_employee, Lecturer):
                        val = float(input("Nhập phần trăm tiến độ KPI: "))
                        current_employee.update_kpi(val)
                else:
                    print("Lựa chọn không hợp lệ.")
            except ValueError as e:
                print(f"Lỗi Dữ Liệu: {e}")

        elif choice == '4':
            if not current_employee:
                continue
            salary = current_employee.calculate_salary()
            print(f"\nTổng lương thực nhận tháng này: {salary:,.0f} VND")

        elif choice == '5':
            if len(employees) < 2:
                print("Cần ít nhất 2 nhân sự.")
                continue
            
            print("Danh sách nhân sự khác:")
            for idx, emp in enumerate(employees):
                if emp != current_employee:
                    print(f"{idx}. {emp.emp_code}")
            
            try:
                target_idx = int(input("Chọn ID nhân sự đối ứng: "))
                other = employees[target_idx]
                
                is_less = current_employee < other
                total_hours = current_employee + other
                
                if is_less is not NotImplemented:
                    compare_str = "ÍT HƠN" if is_less else "KHÔNG ÍT HƠN"
                    print(f"[Kết quả So sánh]: Nhân sự A {compare_str} nhân sự B.")
                    print(f"[Kết quả Tổng hợp]: {total_hours} giờ.")
            except (ValueError, IndexError):
                print("Lỗi thao tác.")

        elif choice == '6':
            if not current_employee:
                continue
            print("1. Vietcombank | 2. Techcombank | 3. Lỗi giả lập")
            bank_choice = input("Chọn cổng ngân hàng (1-3): ")
            salary = current_employee.calculate_salary()
            
            if bank_choice == '1':
                execute_payroll(VietcombankCorporateService(), current_employee, salary)
            elif bank_choice == '2':
                execute_payroll(TechcombankCorporateService(), current_employee, salary)
            elif bank_choice == '3':
                class InvalidBank: pass
                execute_payroll(InvalidBank(), current_employee, salary)

        elif choice == '7':
            break

if __name__ == "__main__":
    main()