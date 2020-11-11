from IPython.display import display, HTML
from builtins import print as original_print

STYLE = r"""<style type="text/css">
td, th, table {
    text-align: center !important;
    background-color: #ffffff;
}
th {
    border: 1px solid black !important;
}
</style>"""

KARNAUGH = {
    1 : r"""<table>
            <tr><td colspan=2>{2}</td></tr>
            <tr><td>0</td><td>1</td></tr>
            <tr><th>{0}</th><th>{1}</th></tr>
        </table>""",
    2 : r"""<table>
            <tr><td rowspan="2" colspan="2"></td><td colspan=2>{5}</td></tr>
            <tr><td>0</td><td>1</td></tr>
            <tr><td rowspan=2>{4}</td><td>0</td><th>{0}</th><th>{1}</th></tr>
            <tr><td>1</td><th>{2}</th><th>{3}</th></tr>
        </table>""",
    3 : r"""<table>
            <tr><td rowspan="2" colspan="2"></td><td colspan=4>{9}{10}</td></tr>
            <tr><td>00</td><td>01</td><td>11</td><td>10</td></tr>
            <tr><td rowspan=2>{8}</td><td>0</td><th>{0}</th><th>{1}</th><th>{3}</th><th>{2}</th></tr>
            <tr><td>1</td><th>{4}</th><th>{5}</th><th>{7}</th><th>{6}</th></tr>
        </table>""",
    4 : r"""<table>
            <tr><td rowspan="2" colspan="2"></td><td colspan=4>{18}{19}</td></tr>
            <tr><td>00</td><td>01</td><td>11</td><td>10</td></tr>
            <tr><td rowspan=4>{16}{17}</td><td>00</td><th>{0}</th><th>{1}</th><th>{3}</th><th>{2}</th></tr>
            <tr><td>01</td><th>{4}</th><th>{5}</th><th>{7}</th><th>{6}</th></tr>
            <tr><td>11</td><th>{12}</th><th>{13}</th><th>{15}</th><th>{14}</th></tr>
            <tr><td>10</td><th>{8}</th><th>{9}</th><th>{11}</th><th>{10}</th></tr>
        </table>""",
    5 : r"""<table>
            <tr><td colspan="2"></td><td colspan="4">{32}=0</td><td rowspan="7"></td><td colspan="4">{32}=1</td></tr>
            <tr><td rowspan="2" colspan="2"></td><td colspan=4>{35}{36}</td>    <td colspan=4>{35}{36}</td></tr>
            <tr><td>00</td><td>01</td><td>11</td><td>10</td>    <td>00</td><td>01</td><td>11</td><td>10</td></tr>
            <tr><td rowspan=4>{33}{34}</td><td>00</td><th>{0}</th><th>{1}</th><th>{3}</th><th>{2}</th>    <th>{16}</th><th>{17}</th><th>{19}</th><th>{18}</th></tr>
            <tr><td>01</td><th>{4}</th><th>{5}</th><th>{7}</th><th>{6}</th>    <th>{20}</th><th>{21}</th><th>{23}</th><th>{22}</th></tr>
            <tr><td>11</td><th>{12}</th><th>{13}</th><th>{15}</th><th>{14}</th>    <th>{28}</th><th>{29}</th><th>{31}</th><th>{30}</th></tr>
            <tr><td>10</td><th>{8}</th><th>{9}</th><th>{11}</th><th>{10}</th>    <th>{24}</th><th>{25}</th><th>{27}</th><th>{26}</th></tr>
        </table>""",
    6 : r"""<table>
            <tr><td rowspan="3"></td><td colspan="2"></td><td colspan="4">{65}=0</td><td rowspan="7"></td><td colspan="4">{65}=1</td></tr>
            <tr><td rowspan="2" colspan="2"></td><td colspan=4>{68}{69}</td>    <td colspan=4>{68}{69}</td></tr>
            <tr><td>00</td><td>01</td><td>11</td><td>10</td>    <td>00</td><td>01</td><td>11</td><td>10</td></tr>
            <tr><td rowspan="4">{64}=0</td><td rowspan=4>{66}{67}</td><td>00</td><th>{0}</th><th>{1}</th><th>{3}</th><th>{2}</th>    <th>{16}</th><th>{17}</th><th>{19}</th><th>{18}</th></tr>
            <tr><td>01</td><th>{4}</th><th>{5}</th><th>{7}</th><th>{6}</th>    <th>{20}</th><th>{21}</th><th>{23}</th><th>{22}</th></tr>
            <tr><td>11</td><th>{12}</th><th>{13}</th><th>{15}</th><th>{14}</th>    <th>{28}</th><th>{29}</th><th>{31}</th><th>{30}</th></tr>
            <tr><td>10</td><th>{8}</th><th>{8}</th><th>{11}</th><th>{10}</th>    <th>{24}</th><th>{25}</th><th>{27}</th><th>{26}</th></tr>
            <tr><td colspan="12"></td></tr>
            <tr><td rowspan="4">{64}=1</td><td rowspan=4>{66}{67}</td><td>00</td><th>{32}</th><th>{33}</th><th>{35}</th><th>{34}</th><td rowspan="5"></td><th>{48}</th><th>{49}</th><th>{51}</th><th>{50}</th></tr>
            <tr><td>01</td><th>{36}</th><th>{37}</th><th>{39}</th><th>{38}</th>    <th>{52}</th><th>{53}</th><th>{55}</th><th>{54}</th></tr>
            <tr><td>11</td><th>{44}</th><th>{45}</th><th>{47}</th><th>{46}</th>    <th>{60}</th><th>{61}</th><th>{63}</th><th>{62}</th></tr>
            <tr><td>10</td><th>{40}</th><th>{41}</th><th>{43}</th><th>{42}</th>    <th>{56}</th><th>{57}</th><th>{59}</th><th>{58}</th></tr>
        </table>"""
}

def run(variables,*args):
    display( HTML(STYLE + KARNAUGH[variables].format(*args)) )
