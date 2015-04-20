ECHO Start of Loop

FOR /L %i IN (1,1,1) DO (
  ECHO %i
  "C:\Users\Kathleen Mullins\AppData\Local\OzoneSoft\ContextFree\ContextFreeCLI.exe" /s400 /c "\\vmware-host\Shared Folders\Documents\2015\School\CS-DirectedStudy\Computer-Embroidery\out\cfa\picasso.cfdg" "\\vmware-host\Shared Folders\Documents\2015\School\CS-DirectedStudy\Computer-Embroidery\out\img\%i%.png"
)