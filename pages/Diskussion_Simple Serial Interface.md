# Diskussion:Simple Serial Interface

- Kann es sein, dass die Pinbelegung für den Anschluss an die Betty nicht richtig ist??

  
Müsste glaub so sein...

              +----+
      VCC -- 6|O  O|5 -- GND
    EINT1 -- 4|O  O|3 -- RESET
       Tx -- 2|O  O|1 -- Rx
              +----+

Hi nein ist sie nicht ist so wie der Entwickler der Schaltung es für am besten hielt musst halt die Adern dann im Verbindungskabel drehen. --Theborg 05:51, 5 December 2007 (CET)

  
Ok. ich dachte, der Stecker sei dafür ausgelegt, dass er diekt an die FB gesteckt wird - Klar, so ist's natürlich egal, wie er belegt ist! Sorry :-) --Tobi 20:22, 5 December 2007 (CET)

  
da es scheinbar sehr viele leute stört, obgleich ich es schaltungstechnisch so einfacher fand, werde ich wohl demnächst in der nächsten revision den kritiken nachkommen und es betty-konform machen... aber jedem kann man es nicht recht machen, in der neuen version soll das ding ja auch mit dem ip-adapter funktionieren (tut es im grunde ja jetzt schon) aber der hat wieder eine ganz andere belegung. wie mans macht... --[Alterego](Benutzer_Alterego.md "Benutzer:Alterego") 05:47, 6 December 2007 (CET)

  
also ich hab mir jetzt einpin steker drauf gemacht so kan ich es auf jedem geret anstöpseln das einzige was eigentlich am interface fehlt ist der pullup für den ip-adapter der nicht mal die funktion beeintrechtigen würde mamala wil das ja dan auch passend in der sw einbauen auserdem muss man den net jumpern wie bei dem anderen interface--Theborg 22:24, 6 December 2007 (CET)

  
klar würde der pullup stören, denn der würde dann ja dafür sorgen das es an der betty nimmer geht, ob pullup genuzt wird also HIGH pegel, oder ob LOW pegel muss sehr wohl mit nem jumper gelöst werden, wie willst du das sonst machen? --[Alterego](Benutzer_Alterego.md "Benutzer:Alterego") 10:25, 7 December 2007 (CET)

  
wieso wuerde der stoeren? in der betty selber sind ja ebenfalls pullups auf eint & reset. und wen der transistor/fet schaltet, zieht er halt auf masse. lediglich in der software muss dann der level fuer eitn bzw. dann boot (fuer ip-adapter) invertiert werden. --[Netguy](Benutzer_Netguy.md "Benutzer:Netguy")

  
ok. ich hab in zwischen n bissel drüber nahcgedacht und nun verstanden was ihr meint... ich werd das nun mal genau so umsetzen. eine gute idee. weiss jmd wie gross die pullups in betty und im ip adapter sind? Ich denke daran erstmal pauschal 1k widerstände rein zu machen. --[Alterego](Benutzer_Alterego.md "Benutzer:Alterego") 04:16, 12 December 2007 (CET)

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

