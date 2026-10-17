# MSP430 Pin-Belegung

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
<td>P1.0</td>
<td>13</td>
<td>TACLK</td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td></td>
<td>CS</td>
<td>Funkmodul Chip-Select</td>
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
<td>15</td>
<td>TA1</td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td></td>
<td>MOSI</td>
<td>Funkmodul Eingang Daten</td>
</tr>
<tr>
<td>P1.3</td>
<td>16</td>
<td>TA2</td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td></td>
<td>MISO</td>
<td>Funkmodul Ausgang Daten</td>
</tr>
<tr>
<td>P1.4</td>
<td>17</td>
<td>SMCLK<br />
TCK</td>
<td>O</td>
<td>=</td>
<td>ISP<br />
Watchdog</td>
<td></td>
<td></td>
<td>Reset externer Watchdog</td>
</tr>
<tr>
<td>P1.5</td>
<td>18</td>
<td>TA0<br />
TMS</td>
<td>O</td>
<td>=</td>
<td>ISP<br />
PWR</td>
<td></td>
<td></td>
<td>CC1100 power</td>
</tr>
<tr>
<td>P1.6</td>
<td>20</td>
<td>TA1<br />
TDI<br />
TCLK</td>
<td>O</td>
<td>=</td>
<td>ISP<br />
PWR</td>
<td></td>
<td></td>
<td>extra current</td>
</tr>
<tr>
<td>P1.7</td>
<td>21</td>
<td>TA2<br />
TD0<br />
TDI</td>
<td>O</td>
<td>=</td>
<td>ISP<br />
PWR</td>
<td></td>
<td></td>
<td>CC1100 auxiliary power</td>
</tr>
<tr>
<td>P2.0</td>
<td>6</td>
<td>ACLK</td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>P2.1</td>
<td>7</td>
<td>INCLK</td>
<td>I</td>
<td>=</td>
<td>ARM</td>
<td></td>
<td>ARM_CLK</td>
<td></td>
</tr>
<tr>
<td>P2.2</td>
<td>8</td>
<td>CAOUT<br />
TA0</td>
<td>I</td>
<td>=</td>
<td>ARM</td>
<td></td>
<td>ARM_MOSI</td>
<td></td>
</tr>
<tr>
<td>P2.3</td>
<td>10</td>
<td>CA0<br />
TA1</td>
<td>O</td>
<td>=</td>
<td>ARM</td>
<td></td>
<td>ARM_MISO</td>
<td></td>
</tr>
<tr>
<td>P2.4</td>
<td>11</td>
<td>CA1<br />
TA2</td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td>ADC_IN1</td>
<td></td>
</tr>
<tr>
<td>P2.5</td>
<td>24</td>
<td>ROSC</td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td>LINE_CONTROL</td>
<td></td>
</tr>
</tbody>
</table>

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

