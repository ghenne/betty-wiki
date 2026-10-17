# P89LPC931 Pin-Belegung

<table data-align="left" data-border="1" data-cellpadding="5" data-cellspacing="0">
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<th>Port</th>
<th>Pin</th>
<th>Funktion</th>
<th>Dir</th>
<th>=</th>
<th>Ziel</th>
<th>Pin</th>
<th>Funktion</th>
<th>Beschreibung</th>
</tr>
&#10;<tr>
<td>P0.0</td>
<td>3</td>
<td>CMP2<br />
KBI0</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P0.1</td>
<td>26</td>
<td>CIN2B<br />
KBI1</td>
<td></td>
<td>=</td>
<td>CC1100</td>
<td>7</td>
<td>CSn</td>
<td>Funkmodul Chip-Select</td>
</tr>
<tr>
<td>P0.2</td>
<td>25</td>
<td>CIN2A<br />
KBI2</td>
<td></td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P0.3</td>
<td>24</td>
<td>CIN1B<br />
KBI3</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P0.4</td>
<td>23</td>
<td>CIN1A<br />
KBI4</td>
<td>I/O</td>
<td>=</td>
<td>ISP HEADER<br />
EPM3064A</td>
<td>5<br />
_</td>
<td>PDA<br />
_</td>
<td>Serial data I/O for programming communication<br />
_</td>
</tr>
<tr>
<td>P0.5</td>
<td>22</td>
<td>CMPREF<br />
KBI5</td>
<td>I</td>
<td>=</td>
<td>ISP HEADER</td>
<td>4</td>
<td>PCL</td>
<td>Serial clock input for programming communication.</td>
</tr>
<tr>
<td>P0.6</td>
<td>20</td>
<td>CMP1<br />
KBI6</td>
<td></td>
<td>=</td>
<td>CC1100</td>
<td>6</td>
<td>GDO0</td>
<td>Funkmodul Universal-I/O 1</td>
</tr>
<tr>
<td>P0.7</td>
<td>19</td>
<td>T1<br />
KBI7</td>
<td></td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P1.0</td>
<td>18</td>
<td>TXD</td>
<td>O</td>
<td>=</td>
<td>ISP HEADER<br />
LED</td>
<td>2<br />
_</td>
<td>TXD<br />
LED</td>
<td></td>
</tr>
<tr>
<td>P1.1</td>
<td>14</td>
<td>TA0</td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td></td>
<td>SCLK</td>
<td>Funkmodul Eingang Takt</td>
</tr>
<tr>
<td>P1.2</td>
<td>12</td>
<td>T0<br />
SCL</td>
<td>O</td>
<td>=</td>
<td>24C64AN</td>
<td></td>
<td>SCL</td>
<td>I2C Takt</td>
</tr>
<tr>
<td>P1.3</td>
<td>11</td>
<td>INT0<br />
SDA</td>
<td>I/O</td>
<td>=</td>
<td>24C64AN</td>
<td></td>
<td>SDA</td>
<td>I2C Daten</td>
</tr>
<tr>
<td>P1.4</td>
<td>10</td>
<td>INT1</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P1.5</td>
<td>6</td>
<td>RST</td>
<td>I</td>
<td>=</td>
<td>CC1100</td>
<td>2</td>
<td>MISO</td>
<td>Funkmodul Ausgang Daten</td>
</tr>
<tr>
<td>P1.6</td>
<td>5</td>
<td>P1.6</td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td>20</td>
<td>MOSI</td>
<td>Funkmodul Eingang Daten</td>
</tr>
<tr>
<td>P1.7</td>
<td>4</td>
<td>P1.7</td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td>1</td>
<td>SCLK</td>
<td>Funkmodul Eingang Takt</td>
</tr>
<tr>
<td>P2.0</td>
<td>1</td>
<td>P2.0</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.1</td>
<td>2</td>
<td>P2.1</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.2</td>
<td>13</td>
<td>SPI_MOSI</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.3</td>
<td>14</td>
<td>SPI_MISO</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.4</td>
<td>15</td>
<td>SPI_SS</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.5</td>
<td>16</td>
<td>SPI_CLK</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.6</td>
<td>27</td>
<td>P2.6</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.7</td>
<td>28</td>
<td>P2.7</td>
<td></td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P3.0</td>
<td>9</td>
<td>XTAL2<br />
CLKOUT</td>
<td></td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P3.1</td>
<td>8</td>
<td>XTAL1<br />
CLKIN</td>
<td>I</td>
<td>=</td>
<td>EPM3064A</td>
<td></td>
<td>CLK OUT</td>
<td>Prozessor Takt</td>
</tr>
</tbody>
</table>

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

