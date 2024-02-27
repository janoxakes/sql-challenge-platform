from authentication import Authenticator
from backend import ChallengeDB, BackendDB
from frontend import UI
import logging

def auth():
    backend = BackendDB()
    auth = Authenticator(backend)
    auth.show_login_form()

def main():
    ui = UI()
    dbh = ChallengeDB()

    ui.display_header_and_desc()
    query_input = ui.display_query_area()
    
    col1, col2, col3 = ui.init_3_columns()
    with col1:
        run_query = ui.display_run_query_buttons()
    with col2:
        validate_query = ui.display_validate_query_button()
    with col3:
        submit_solution = ui.display_submit_button()
    
    if run_query:
        try:
            df_result = dbh.retrive_results(query_input)
            df_result.style.format(precision=6)
            ui.display_table(df_result)
        except dbh.invalid_query_exception as e:
            ui.display_error("The query is invalid")
            logging.error(e)
        except TypeError as e:
            ui.display_error("The query is invalid")
            logging.error(e)
        except Exception as e:
            ui.display_exception(e)
            logging.error(e)

    elif validate_query:
        try:
            df_result = dbh.retrive_results(query_input)
            validation = dbh.compare_solution(query_input, "1")
            if validation:
                ui.display_success("The result is correct")
            else:
                ui.display_error("The result is incorrect")
        except dbh.invalid_query_exception:
            ui.display_error("The query is invalid")
        except TypeError:
            ui.display_error("The query is invalid")
        except Exception as e:
            ui.display_exception(e)
    
    elif submit_solution:
        ui.display_info(f"Submission not implemented yet")

if __name__ == "__main__":
    auth()
    main()
