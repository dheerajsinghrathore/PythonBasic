import os

def read_emp(filename):
    f = None
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        f = open(file_path, "r")
        lines = f.readlines()
        if not lines:
            raise ValueError("File is empty")
        employees = []
        salaries = []
        for line in lines:
            line = line.strip()
            try:
                name, sal = line.split(",")
                sal = eval(sal)
                employees.append((name, sal))
                salaries.append(sal)
            except ValueError:
                print(f"Skipping invalid line:{line}")
        if not employees:
            raise ValueError("No valid employee data found ")
        print("\nEmployee Data")
        for emp in employees:
            print(f"Name:{emp[0]},Sal:{emp[1]}")

        highest = max(salaries)
        lowest = min(salaries)
        avg = sum(salaries) / len(salaries)
        print(f"\nHighest salary{highest}")
        print(f"\nLowest salary{lowest}")
        print(f"\nAvg salary{avg}")
    except FileNotFoundError:
        print("Error ! Cannot find the file")
    except OSError as ex1:
        print("Error!", ex1)
    except ValueError as ex2:
        print("Error:", ex2)
    except Exception as ex3:
        print("Unexpected error", ex3)
    finally:
        if f is not None:
            f.close()
            print("\nFile closed successfully")


read_emp("emp.csv")
