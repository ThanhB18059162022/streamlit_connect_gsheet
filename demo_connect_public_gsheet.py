import streamlit as st

st.subheader("📗 Google Sheets st.connection using Public URLs")

url = "https://docs.google.com/spreadsheets/d/17h2EbQvMf0bFhkgrAQaFaXxN33rc5t7ssp6fJPmHdXM/edit?gid=448791162#gid=448791162"

st.write("#### 1. Read public Google Worksheet as Pandas")

with st.echo():
    import streamlit as st

    from streamlit_gsheets import GSheetsConnection

    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(spreadsheet=url, worksheet="Y tế Thay đổi quy định", usecols=[0, 1])
    st.dataframe(df)

st.write("#### 2. Query public Google Worksheet using SQL")
st.info(
    "Mutation SQL queries are in-memory only and do not results in the Worksheet update.",
    icon="ℹ️",  # noqa: RUF001
)
st.warning(
    """You can query only one Worksheet in provided public Spreadsheet,
        use Worksheet name as target in from SQL queries.
        The worksheet, which you query is defined by GID query parameter or GID parameters to query method.""",
    icon="⚠️",
)


with st.echo():
    import streamlit as st

    from streamlit_gsheets import GSheetsConnection

    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.query('select * from "Y tế Thay đổi quy định" limit 10', spreadsheet=url)
    st.dataframe(df)