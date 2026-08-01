# Constants define kora bhalo practice
LOG_FILE = 'code_with_harry\\file_io\\3\\server.log'
REPORT_FILE = 'error_report.txt'

def generate_error_report():
    error_count = 0
    component_counts = {}
    error_lines = []

    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                # 1. Fast Filter: Sudhu ERROR line process korbe
                if '[ERROR]' in line:
                    error_count += 1
                    clean_line = line.strip()
                    error_lines.append(clean_line)

                    # 2. Extract Component: '[DB]' ba '[AUTH]' ber kora
                    # Logic: ERROR er porer bit-e component thake
                    parts = clean_line.split('] [')
                    if len(parts) > 2:
                        # parts[2] hobe "DB] - Message..."
                        component = parts[2].split(']')[0] 
                        
                        # Dictionary Update (Fastest way)
                        component_counts[component] = component_counts.get(component, 0) + 1

        # 3. Write Report
        with open(REPORT_FILE, 'w') as out:
            out.write("--- Error Analysis Report ---\n")
            out.write(f"Total Errors Found: {error_count}\n\n")
            
            out.write("Errors by Component:\n")
            for comp, count in component_counts.items():
                out.write(f"- {comp}: {count}\n")
            
            out.write("\nDetailed Error Logs:\n")
            for i, log in enumerate(error_lines, 1):
                out.write(f"{i}. {log}\n")
            
            out.write("-----------------------------")
            
        print(f"Success! Report saved in {REPORT_FILE}")

    except FileNotFoundError:
        print("Error: log file-ti khuje paoa jayni.")

if __name__ == "__main__":
    generate_error_report()
        