import streamlit as st

class UI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title = "SQL Challenge"
        )
    
    def display_header_and_desc(self):
        # refactor to use for any number of challenges
        st.title("SQL Challage #1")
        st.write("""
        ### #1 For the following tables: invoices and customers
        
        Select customer countries that contain the letter 'u' where the total (2 digits precision) is greater than 100
        * Expected columns name Country and Total (case sensitive)
        """)

    def display_query_area(self):
        return st.text_area("Enter your query here:", height=300, value="SELECT * FROM customers")

    def init_3_columns(self):
        return st.columns(3)

    def display_run_query_buttons(self):
        return st.button("Run query")

    def display_validate_query_button(self):
        return st.button("Validate result")

    def display_submit_button(self):
        return st.button("Submit solution")

    def display_msg(self, msg):
        st.write(msg)

    def display_table(self, df):
        st.dataframe(df, hide_index=True)
    
    def display_success(self, msg):
        st.success(msg)
        st.balloons()

    def display_info(self, msg):
        st.info(msg)

    def display_error(self, msg):
        st.error(msg)

    def display_exception(self, e):
        st.exception(e)

if __name__ == "__main__":
    pass