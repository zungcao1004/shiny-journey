from window_handler import get_captcha_pattern, monitor_and_solve_captcha
def main():
    process_name = "so2game.exe"
    # get_captcha_pattern(process_name, 0.1)
    monitor_and_solve_captcha(process_name, 0.4)

main()