# LPC2220 Pin-Belegung

Diese Übersicht befindet sich noch im Aufbau!

Für Funktionen in **Bold** wird die entsprechende Hardwarefunktion des Pin´s verwendet.

Anregungen, Fehler und sonstiges bitte hier diskutieren:

[\[../forum/topics/0140-lpc2220-pin-belegung.md](../forum/topics/0140-lpc2220-pin-belegung.md)\]

Danke pcsquirrel

  

## Bekannte Pins

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
<td>P0.00</td>
<td>42</td>
<td><strong>TXD0</strong><span class="small"><br />
</span><span class="small">PWM1</span></td>
<td>O</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>12</td>
<td>TxD</td>
<td>ISP/Bootloader TxD</td>
</tr>
<tr>
<td>P0.01</td>
<td>49</td>
<td><strong>RXD0</strong><span class="small"><br />
</span><span class="small">PWM3</span><span class="small"><br />
</span><span class="small">EINT0</span></td>
<td>I</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>11</td>
<td>RxD</td>
<td>ISP/Bootloader RxD</td>
</tr>
<tr>
<td>P0.02</td>
<td>50</td>
<td><strong>SCL</strong><span class="small"><br />
</span><span class="small">CAP0.0</span></td>
<td>O</td>
<td>=</td>
<td>PCF8563</td>
<td>6</td>
<td>SCL</td>
<td>RTC/Echtzeituhr I2C Takt</td>
</tr>
<tr>
<td>P0.03</td>
<td>58</td>
<td><strong>SDA</strong><span class="small"><br />
</span><span class="small">MAT0.0</span><span class="small"><br />
</span><span class="small">EINT1</span></td>
<td>I/O</td>
<td>=</td>
<td>PCF8563</td>
<td>5</td>
<td>SDA</td>
<td>RTC/Echtzeituhr I2C Daten</td>
</tr>
<tr>
<td>P0.04</td>
<td>59</td>
<td><span class="small">SCK0</span><span class="small"><br />
</span><span class="small">CAP0.1</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>LCD Backlight</td>
</tr>
<tr>
<td>P0.05</td>
<td>61</td>
<td><span class="small">MISO0</span><span class="small"><br />
</span><span class="small">MAT0.1</span></td>
<td>?</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Erkennung der Hardwareversion der Betty</td>
</tr>
<tr>
<td>P0.06</td>
<td>68</td>
<td><span class="small">MOSI0</span><span class="small"><br />
</span><span class="small"></span></td>
<td>?</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>SOUND ON</td>
</tr>
<tr>
<td>P0.07</td>
<td>69</td>
<td><span class="small">SSEL0</span><span class="small"><br />
</span><strong>PWM2</strong><span class="small"><br />
</span><span class="small">EINT2</span></td>
<td>O</td>
<td>=</td>
<td>LM4786</td>
<td>4</td>
<td>+IN</td>
<td>Audio PWM</td>
</tr>
<tr>
<td>P0.08</td>
<td>75</td>
<td><strong>TXD1</strong><span class="small"><br />
</span><span class="small">PWM4</span></td>
<td>O</td>
<td>=</td>
<td><a href="SLE%2066C24PE.md" title="SLE 66C24PE">SLE 66C24PE</a></td>
<td>3</td>
<td>Data</td>
<td>Smartcardchip Data I/O (Die Datenrate ist 1/64 der Taktfrequenz, also 58593,75 Bit/s. Bei 7.5 Mhz CLK)</td>
</tr>
<tr>
<td>P0.09</td>
<td>76</td>
<td><strong>RXD1</strong><span class="small"><br />
</span><span class="small">PWM6</span><span class="small"><br />
</span><span class="small">EINT3</span></td>
<td>I</td>
<td>=</td>
<td><a href="SLE%2066C24PE.md" title="SLE 66C24PE">SLE 66C24PE</a></td>
<td>3</td>
<td>Data</td>
<td>Smartcardchip Data I/O (Die Datenrate ist 1/64 der Taktfrequenz, also 58593,75 Bit/s. Bei 7.5 Mhz CLK)</td>
</tr>
<tr>
<td>P0.10</td>
<td>78</td>
<td><span class="small">RTS1</span><span class="small"><br />
</span><span class="small">CAP1.0</span></td>
<td>O</td>
<td>=</td>
<td><a href="SLE%2066C24PE.md" title="SLE 66C24PE">SLE 66C24PE</a></td>
<td>8</td>
<td>Power</td>
<td>Smartcardchip Stromversorgung - invertiert (CPU-Pin LOW =&gt; Power HIGH)</td>
</tr>
<tr>
<td>P0.11</td>
<td>83</td>
<td><span class="small">CTS1</span><span class="small"><br />
</span><span class="small">CAP1.1</span></td>
<td>O</td>
<td>=</td>
<td>LM4786</td>
<td>1</td>
<td>/SHUTDOWN</td>
<td>Audio Shutdown</td>
</tr>
<tr>
<td>P0.12</td>
<td>84</td>
<td><span class="small">DSR1</span><span class="small"><br />
</span><span class="small">MAT1.0</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>IR Empfang aktivieren</td>
</tr>
<tr>
<td>P0.13</td>
<td>85</td>
<td><span class="small">DTR1</span><span class="small"><br />
</span><span class="small">MAT1.1</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P0.14</td>
<td>92</td>
<td><span class="small">DCD1</span><span class="small"><br />
</span><span class="small">EINT1</span></td>
<td>I</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>10</td>
<td>/Bootloader EN</td>
<td>ISP/Bootloader Enable</td>
</tr>
<tr>
<td>P0.15</td>
<td>99</td>
<td><span class="small">RI1</span><span class="small"><br />
</span><strong>EINT2</strong></td>
<td>I</td>
<td>=</td>
<td>PCF8563</td>
<td>3</td>
<td>/INT</td>
<td>RTC/Echtzeituhr Interruptausgang (Programmierbar)</td>
</tr>
<tr>
<td>P0.16</td>
<td>100</td>
<td><span class="small">EINT0</span><span class="small"><br />
</span><span class="small">MAT0.2</span><span class="small"><br />
</span><span class="small">CAP0.2</span></td>
<td>?</td>
<td>=</td>
<td>CC1100</td>
<td>6</td>
<td>GDO0</td>
<td>Funkmodul Universal-I/O 1</td>
</tr>
<tr>
<td>P0.17</td>
<td>101</td>
<td><span class="small">CAP1.2</span><span class="small"><br />
</span><strong>SCK1</strong><span class="small"><br />
</span><span class="small">MAT1.2</span></td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td>1</td>
<td>SCLK</td>
<td>Funkmodul Eingang Takt</td>
</tr>
<tr>
<td>P0.18</td>
<td>121</td>
<td><span class="small">CAP1.3</span><span class="small"><br />
</span><strong>MISO1</strong><span class="small"><br />
</span><span class="small">MAT1.3</span></td>
<td>I</td>
<td>=</td>
<td>CC1100</td>
<td>2</td>
<td>MISO</td>
<td>Funkmodul Ausgang Daten</td>
</tr>
<tr>
<td>P0.19</td>
<td>122</td>
<td><span class="small">MAT1.2</span><span class="small"><br />
</span><strong>MOSI1</strong><span class="small"><br />
</span><span class="small">CAP1.2</span></td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td>20</td>
<td>MOSI</td>
<td>Funkmodul Eingang Daten</td>
</tr>
<tr>
<td>P0.21</td>
<td>4</td>
<td><span class="small">PWM5</span><span class="small"><br />
</span><span class="small">CAP1.3</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>IR Sendediode</td>
</tr>
<tr>
<td>P0.22</td>
<td>5</td>
<td><span class="small">CAP0.0</span><span class="small"><br />
</span><span class="small">MAT0.0</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P0.23</td>
<td>6</td>
<td></td>
<td>O</td>
<td>=</td>
<td>CC1100</td>
<td>7</td>
<td>CSn</td>
<td>Funkmodul Chip-Select</td>
</tr>
<tr>
<td>P0.24</td>
<td>8</td>
<td></td>
<td>?</td>
<td>=</td>
<td>CC1100</td>
<td>3</td>
<td>GDO2</td>
<td>Funkmodul Universal-I/O 3</td>
</tr>
<tr>
<td>P0.27</td>
<td>23</td>
<td><span class="small">AIN0</span><span class="small"><br />
</span><span class="small">CAP0.1</span><span class="small"><br />
</span><span class="small">MAT0.1</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P0.28</td>
<td>25</td>
<td><span class="small">AIN1</span><span class="small"><br />
</span><span class="small">CAP0.2</span><span class="small"><br />
</span><span class="small">MAT0.2</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P0.29</td>
<td>32</td>
<td><span class="small">AIN2</span><span class="small"><br />
</span><span class="small">CAP0.3</span><span class="small"><br />
</span><span class="small">MAT0.3</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>IR Empfang Capture</td>
</tr>
<tr>
<td>P0.30</td>
<td>33</td>
<td><span class="small">AIN3</span><span class="small"><br />
</span><strong>EINT3</strong><span class="small"><br />
</span><span class="small">CAP0.0</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Interrupt</td>
</tr>
<tr>
<td>P1.00</td>
<td>91</td>
<td><strong>CS0</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>Chip Enable</td>
<td>Bank 0 Flash 0 0x8000 0000 - 0x8007 FFFF</td>
</tr>
<tr>
<td>P1.01</td>
<td>90</td>
<td><strong>OE</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>OE</td>
<td></td>
</tr>
<tr>
<td>P1.01</td>
<td>90</td>
<td><strong>OE</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>OE</td>
<td></td>
</tr>
<tr>
<td>P1.26</td>
<td>52</td>
<td><strong>RTCK</strong></td>
<td>I/O</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>4</td>
<td>JTAG RTCK</td>
<td>JTAG</td>
</tr>
<tr>
<td>P1.27</td>
<td>144</td>
<td><strong>TDO</strong></td>
<td>O</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>2</td>
<td>JTAG TDO</td>
<td>JTAG</td>
</tr>
<tr>
<td>P1.28</td>
<td>140</td>
<td><strong>TDI</strong></td>
<td>I</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>3</td>
<td>JTAG TDI</td>
<td>JTAG</td>
</tr>
<tr>
<td>P1.29</td>
<td>126</td>
<td><strong>TCK</strong></td>
<td>I</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>6</td>
<td>JTAG TCK</td>
<td>JTAG</td>
</tr>
<tr>
<td>P1.30</td>
<td>113</td>
<td><strong>TMS</strong></td>
<td>I</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>1</td>
<td>JTAG TMS</td>
<td>JTAG</td>
</tr>
<tr>
<td>P1.31</td>
<td>43</td>
<td><strong>TRST</strong></td>
<td>I</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>5</td>
<td>JTAG nTRST</td>
<td>JTAG</td>
</tr>
<tr>
<td>P2.00</td>
<td>98</td>
<td><strong>D0</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D0</td>
<td></td>
</tr>
<tr>
<td>P2.00</td>
<td>98</td>
<td><strong>D0</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D0</td>
<td></td>
</tr>
<tr>
<td>P2.00</td>
<td>98</td>
<td><strong>D0</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D0</td>
<td></td>
</tr>
<tr>
<td>P2.01</td>
<td>105</td>
<td><strong>D1</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D1</td>
<td></td>
</tr>
<tr>
<td>P2.01</td>
<td>105</td>
<td><strong>D1</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D1</td>
<td></td>
</tr>
<tr>
<td>P2.01</td>
<td>105</td>
<td><strong>D1</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D1</td>
<td></td>
</tr>
<tr>
<td>P2.02</td>
<td>106</td>
<td><strong>D2</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D2</td>
<td></td>
</tr>
<tr>
<td>P2.02</td>
<td>106</td>
<td><strong>D2</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D2</td>
<td></td>
</tr>
<tr>
<td>P2.02</td>
<td>106</td>
<td><strong>D2</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D2</td>
<td></td>
</tr>
<tr>
<td>P2.03</td>
<td>108</td>
<td><strong>D3</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D3</td>
<td></td>
</tr>
<tr>
<td>P2.03</td>
<td>108</td>
<td><strong>D3</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D3</td>
<td></td>
</tr>
<tr>
<td>P2.03</td>
<td>108</td>
<td><strong>D3</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D3</td>
<td></td>
</tr>
<tr>
<td>P2.04</td>
<td>109</td>
<td><strong>D4</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D4</td>
<td></td>
</tr>
<tr>
<td>P2.04</td>
<td>109</td>
<td><strong>D4</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D4</td>
<td></td>
</tr>
<tr>
<td>P2.04</td>
<td>109</td>
<td><strong>D4</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D4</td>
<td></td>
</tr>
<tr>
<td>P2.05</td>
<td>114</td>
<td><strong>D5</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D5</td>
<td></td>
</tr>
<tr>
<td>P2.05</td>
<td>114</td>
<td><strong>D5</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D5</td>
<td></td>
</tr>
<tr>
<td>P2.05</td>
<td>114</td>
<td><strong>D5</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D5</td>
<td></td>
</tr>
<tr>
<td>P2.06</td>
<td>115</td>
<td><strong>D6</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D6</td>
<td></td>
</tr>
<tr>
<td>P2.06</td>
<td>115</td>
<td><strong>D6</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D6</td>
<td></td>
</tr>
<tr>
<td>P2.06</td>
<td>115</td>
<td><strong>D6</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D6</td>
<td></td>
</tr>
<tr>
<td>P2.07</td>
<td>116</td>
<td><strong>D7</strong></td>
<td>I/O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>D7</td>
<td></td>
</tr>
<tr>
<td>P2.07</td>
<td>116</td>
<td><strong>D7</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D7</td>
<td></td>
</tr>
<tr>
<td>P2.07</td>
<td>116</td>
<td><strong>D7</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D7</td>
<td></td>
</tr>
<tr>
<td>P2.08</td>
<td>117</td>
<td><strong>D8</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D8</td>
<td></td>
</tr>
<tr>
<td>P2.08</td>
<td>117</td>
<td><strong>D8</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D8</td>
<td></td>
</tr>
<tr>
<td>P2.09</td>
<td>118</td>
<td><strong>D9</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D9</td>
<td></td>
</tr>
<tr>
<td>P2.09</td>
<td>118</td>
<td><strong>D9</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D9</td>
<td></td>
</tr>
<tr>
<td>P2.10</td>
<td>120</td>
<td><strong>D10</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D10</td>
<td></td>
</tr>
<tr>
<td>P2.10</td>
<td>120</td>
<td><strong>D10</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D10</td>
<td></td>
</tr>
<tr>
<td>P2.11</td>
<td>124</td>
<td><strong>D11</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D11</td>
<td></td>
</tr>
<tr>
<td>P2.11</td>
<td>124</td>
<td><strong>D11</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D11</td>
<td></td>
</tr>
<tr>
<td>P2.12</td>
<td>125</td>
<td><strong>D12</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D12</td>
<td></td>
</tr>
<tr>
<td>P2.12</td>
<td>125</td>
<td><strong>D12</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D12</td>
<td></td>
</tr>
<tr>
<td>P2.13</td>
<td>127</td>
<td><strong>D13</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D13</td>
<td></td>
</tr>
<tr>
<td>P2.13</td>
<td>127</td>
<td><strong>D13</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D13</td>
<td></td>
</tr>
<tr>
<td>P2.14</td>
<td>129</td>
<td><strong>D14</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D14</td>
<td></td>
</tr>
<tr>
<td>P2.14</td>
<td>129</td>
<td><strong>D14</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D14</td>
<td></td>
</tr>
<tr>
<td>P2.15</td>
<td>130</td>
<td><strong>D15</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>D15</td>
<td></td>
</tr>
<tr>
<td>P2.15</td>
<td>130</td>
<td><strong>D15</strong></td>
<td>I/O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>D15</td>
<td></td>
</tr>
<tr>
<td>P2.17</td>
<td>132</td>
<td><strong>D17</strong></td>
<td>O</td>
<td>=</td>
<td><a href="SLE%2066C24PE.md" title="SLE 66C24PE">SLE 66C24PE</a></td>
<td>2</td>
<td>/Reset</td>
<td>Smartcardchip Reset</td>
</tr>
<tr>
<td>P2.18</td>
<td>133</td>
<td><span class="small">D18</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P2.19</td>
<td>134</td>
<td><span class="small">D19</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P2.20</td>
<td>136</td>
<td><span class="small">D20</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P2.21</td>
<td>137</td>
<td><span class="small">D21</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P2.22</td>
<td>1</td>
<td><span class="small">D22</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P2.23</td>
<td>10</td>
<td><span class="small">D23</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P2.24</td>
<td>11</td>
<td><span class="small">D24</span></td>
<td>O</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P2.26</td>
<td>13</td>
<td><span class="small">D26</span><span class="small"><br />
</span><span class="small">BOOT0</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>fix auf Low-Pegel (16 Bit Bootflash on CS0)</td>
</tr>
<tr>
<td>P2.27</td>
<td>16</td>
<td><span class="small">D27</span><span class="small"><br />
</span><span class="small">BOOT1</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>fix auf High-Pegel (16 Bit Bootflash on CS0)</td>
</tr>
<tr>
<td>P2.31</td>
<td>20</td>
<td><span class="small">D31</span><span class="small"><br />
</span><strong>AIN5</strong></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Akkuspannung Analogeingang</td>
</tr>
<tr>
<td>P3.00</td>
<td>89</td>
<td><strong>A0</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A0</td>
<td></td>
</tr>
<tr>
<td>P3.00</td>
<td>89</td>
<td><strong>A0</strong></td>
<td>O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>C/D</td>
<td>0x8100 0000 (Command Mode), 0x8100 0001 (Data Mode)</td>
</tr>
<tr>
<td>P3.00</td>
<td>89</td>
<td><strong>A0</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A0</td>
<td></td>
</tr>
<tr>
<td>P3.01</td>
<td>88</td>
<td><strong>A1</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A1</td>
<td></td>
</tr>
<tr>
<td>P3.01</td>
<td>88</td>
<td><strong>A1</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A1</td>
<td></td>
</tr>
<tr>
<td>P3.02</td>
<td>87</td>
<td><strong>A2</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A2</td>
<td></td>
</tr>
<tr>
<td>P3.02</td>
<td>87</td>
<td><strong>A2</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A2</td>
<td></td>
</tr>
<tr>
<td>P3.03</td>
<td>81</td>
<td><strong>A3</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A3</td>
<td></td>
</tr>
<tr>
<td>P3.03</td>
<td>81</td>
<td><strong>A3</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A3</td>
<td></td>
</tr>
<tr>
<td>P3.04</td>
<td>80</td>
<td><strong>A4</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A4</td>
<td></td>
</tr>
<tr>
<td>P3.04</td>
<td>80</td>
<td><strong>A4</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A4</td>
<td></td>
</tr>
<tr>
<td>P3.05</td>
<td>74</td>
<td><strong>A5</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A5</td>
<td></td>
</tr>
<tr>
<td>P3.05</td>
<td>74</td>
<td><strong>A5</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A5</td>
<td></td>
</tr>
<tr>
<td>P3.06</td>
<td>73</td>
<td><strong>A6</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A6</td>
<td></td>
</tr>
<tr>
<td>P3.06</td>
<td>73</td>
<td><strong>A6</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A6</td>
<td></td>
</tr>
<tr>
<td>P3.07</td>
<td>72</td>
<td><strong>A7</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A7</td>
<td></td>
</tr>
<tr>
<td>P3.07</td>
<td>72</td>
<td><strong>A7</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A7</td>
<td></td>
</tr>
<tr>
<td>P3.08</td>
<td>71</td>
<td><strong>A8</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A8</td>
<td></td>
</tr>
<tr>
<td>P3.08</td>
<td>71</td>
<td><strong>A8</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A8</td>
<td></td>
</tr>
<tr>
<td>P3.09</td>
<td>66</td>
<td><strong>A9</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A9</td>
<td></td>
</tr>
<tr>
<td>P3.09</td>
<td>66</td>
<td><strong>A9</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A9</td>
<td></td>
</tr>
<tr>
<td>P3.10</td>
<td>65</td>
<td><strong>A10</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A10</td>
<td></td>
</tr>
<tr>
<td>P3.10</td>
<td>65</td>
<td><strong>A10</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A10</td>
<td></td>
</tr>
<tr>
<td>P3.11</td>
<td>64</td>
<td><strong>A11</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A11</td>
<td></td>
</tr>
<tr>
<td>P3.11</td>
<td>64</td>
<td><strong>A11</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A11</td>
<td></td>
</tr>
<tr>
<td>P3.12</td>
<td>63</td>
<td><strong>A12</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A12</td>
<td></td>
</tr>
<tr>
<td>P3.12</td>
<td>63</td>
<td><strong>A12</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A12</td>
<td></td>
</tr>
<tr>
<td>P3.13</td>
<td>62</td>
<td><strong>A13</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A13</td>
<td></td>
</tr>
<tr>
<td>P3.13</td>
<td>62</td>
<td><strong>A13</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A13</td>
<td></td>
</tr>
<tr>
<td>P3.14</td>
<td>56</td>
<td><strong>A14</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A14</td>
<td></td>
</tr>
<tr>
<td>P3.14</td>
<td>56</td>
<td><strong>A14</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A14</td>
<td></td>
</tr>
<tr>
<td>P3.15</td>
<td>55</td>
<td><strong>A15</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A15</td>
<td></td>
</tr>
<tr>
<td>P3.15</td>
<td>55</td>
<td><strong>A15</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A15</td>
<td></td>
</tr>
<tr>
<td>P3.16</td>
<td>53</td>
<td><strong>A16</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A16</td>
<td></td>
</tr>
<tr>
<td>P3.16</td>
<td>53</td>
<td><strong>A16</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A16</td>
<td></td>
</tr>
<tr>
<td>P3.17</td>
<td>48</td>
<td><strong>A17</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A17</td>
<td></td>
</tr>
<tr>
<td>P3.17</td>
<td>48</td>
<td><strong>A17</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A17</td>
<td></td>
</tr>
<tr>
<td>P3.18</td>
<td>47</td>
<td><strong>A18</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>A18</td>
<td></td>
</tr>
<tr>
<td>P3.18</td>
<td>47</td>
<td><strong>A18</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>A18</td>
<td></td>
</tr>
<tr>
<td>P3.20</td>
<td>45</td>
<td><span class="small">A20</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P3.21</td>
<td>44</td>
<td><span class="small">A21</span></td>
<td>I</td>
<td>=</td>
<td></td>
<td></td>
<td></td>
<td>Tastatur Row/Col</td>
</tr>
<tr>
<td>P3.23</td>
<td>40</td>
<td><span class="small">A23</span><span class="small"><br />
</span><strong>XCLK</strong></td>
<td>O</td>
<td>=</td>
<td><a href="SLE%2066C24PE.md" title="SLE 66C24PE">SLE 66C24PE</a></td>
<td>7</td>
<td>CLK</td>
<td>Smartcardchip Takt - ist ueber einen externen Frequenzteiler mit dem Takteingang des Chips verbunden. Im Betrieb wird ueber den CPU-Pin der 7,5 MHz Peripherietakt ausgegeben. Durch den Frequenzteiler wird der Takt halbiert. Der Smartcard-Chip wird dadurch mit mit 3,75 MHz getaktet (gilt fÃ¼r Original Firmware)</td>
</tr>
<tr>
<td>P3.25</td>
<td>35</td>
<td><strong>CS2</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>Chip Enable</td>
<td>Bank 2 Flash 1 0x8200 0000 - 0x8207 FFFF</td>
</tr>
<tr>
<td>P3.26</td>
<td>30</td>
<td><strong>CS1</strong></td>
<td>O</td>
<td>=</td>
<td>LCDisplay</td>
<td></td>
<td>Chip Enable</td>
<td>0x8100 0000 (Command Mode), 0x8100 0001 (Data Mode)</td>
</tr>
<tr>
<td>P3.27</td>
<td>29</td>
<td><strong>WE</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 0</td>
<td></td>
<td>WE</td>
<td></td>
</tr>
<tr>
<td>P3.27</td>
<td>29</td>
<td><strong>WE</strong></td>
<td>O</td>
<td>=</td>
<td>EN29LV800 Flash 1</td>
<td></td>
<td>WE</td>
<td></td>
</tr>
<tr>
<td></td>
<td>135</td>
<td><span class="small">/RESET</span></td>
<td>I</td>
<td>=</td>
<td><a href="ISP.md" title="ISP">ISP</a></td>
<td>9</td>
<td>/Reset</td>
<td>ISP/Bootloader /Reset</td>
</tr>
</tbody>
</table>

## Unbenutzte Pins / nicht erfasste Pins

|       |     |                    |     |      |     |          |              |
|-------|-----|--------------------|-----|------|-----|----------|--------------|
| Port  | Pin | Funktion           | =   | Ziel | Pin | Funktion | Beschreibung |
| P0.20 | 123 | MAT1.3/SSEL1/EINT3 | =   |      |     |          |              |
| P0.25 | 21  |                    | =   |      |     |          |              |
| P1.16 | 34  | TRACEPKT0          | =   |      |     |          |              |
| P1.17 | 24  | TRACEPKT1          | =   |      |     |          |              |
| P1.18 | 15  | TRACEPKT2          | =   |      |     |          |              |
| P1.19 | 7   | TRACEPKT3          | =   |      |     |          |              |
| P1.20 | 102 | TRACESYNC          | =   |      |     |          |              |
| P1.21 | 95  | PIPESTAT0          | =   |      |     |          |              |
| P1.22 | 86  | PIPESTAT1          | =   |      |     |          |              |
| P1.23 | 82  | PIPESTAT2          | =   |      |     |          |              |
| P1.24 | 70  | TRACECLK           | =   |      |     |          |              |
| P1.25 | 60  | EXTIN0             | =   |      |     |          |              |
| P2.16 | 131 | D16                | =   |      |     |          |              |
| P2.25 | 12  | D25                | =   |      |     |          |              |
| P2.28 | 17  | D28                | =   |      |     |          |              |
| P2.29 | 18  | D29                | =   |      |     |          |              |
| P2.30 | 19  | D30/AIN4           | =   |      |     |          |              |
| P3.19 | 46  | A19                | =   |      |     |          |              |
| P3.22 | 41  | A22                | =   |      |     |          |              |
| P3.24 | 36  | CS3                | =   |      |     |          |              |
| P3.28 | 28  | BLS3/AIN7          | =   |      |     |          |              |
| P3.29 | 27  | BLS2/AIN6          | =   |      |     |          |              |
| P3.30 | 97  | BLS1               | =   |      |     |          |              |
| P3.31 | 96  | BLS0               | =   |      |     |          |              |
|       | 22  | n.c.               | =   |      |     |          |              |
|       | 142 | XTAL1              | =   |      |     |          |              |
|       | 141 | XTAL2              | =   |      |     |          |              |
|       | 3   | VSS                | =   |      |     |          |              |
|       | 9   | VSS                | =   |      |     |          |              |
|       | 26  | VSS                | =   |      |     |          |              |
|       | 38  | VSS                | =   |      |     |          |              |
|       | 54  | VSS                | =   |      |     |          |              |
|       | 67  | VSS                | =   |      |     |          |              |
|       | 79  | VSS                | =   |      |     |          |              |
|       | 93  | VSS                | =   |      |     |          |              |
|       | 103 | VSS                | =   |      |     |          |              |
|       | 107 | VSS                | =   |      |     |          |              |
|       | 111 | VSS                | =   |      |     |          |              |
|       | 128 | VSS                | =   |      |     |          |              |
|       | 128 | VSS                | =   |      |     |          |              |
|       | 139 | VSSA               | =   |      |     |          |              |
|       | 138 | VSSA(PLL)          | =   |      |     |          |              |
|       | 37  | VDD(1V8)           | =   |      |     |          |              |
|       | 110 | VDD(1V8)           | =   |      |     |          |              |
|       | 143 | VDDA(1V8)          | =   |      |     |          |              |
|       | 2   | VDD(3V3)           | =   |      |     |          |              |
|       | 31  | VDD(3V3)           | =   |      |     |          |              |
|       | 39  | VDD(3V3)           | =   |      |     |          |              |
|       | 51  | VDD(3V3)           | =   |      |     |          |              |
|       | 57  | VDD(3V3)           | =   |      |     |          |              |
|       | 77  | VDD(3V3)           | =   |      |     |          |              |
|       | 94  | VDD(3V3)           | =   |      |     |          |              |
|       | 104 | VDD(3V3)           | =   |      |     |          |              |
|       | 112 | VDD(3V3)           | =   |      |     |          |              |
|       | 119 | VDD(3V3)           | =   |      |     |          |              |
|       | 14  | VDDA(3V3)          | =   |      |     |          |              |

<!-- forum-links:start -->
## Forumsdiskussionen: freie Pins und Erweiterungen

Unbelegte IOs, freie GPIOs sowie SPI- und SD/MMC-Nutzung.

### Freie Pins, GPIOs, SPI, SD/MMC

- [Pinbelegung / unbelegte IOs?](../forum/topics/0122-pinbelegung-unbelegte-ios.md) — Pinbelegung und unbelegte IOs.
- [erweiterung der betty hardware / freie GPIOs](../forum/topics/0278-erweiterung-der-betty-hardware-freie-gpios.md) — Freie GPIOs der Betty für Erweiterungen.
- [Freie Pins, SPI, SD / MMC](../forum/topics/0246-freie-pins-spi-sd-mmc.md) — Freie Pins, SPI und SD/MMC.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

