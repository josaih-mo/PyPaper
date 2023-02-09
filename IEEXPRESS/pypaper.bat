@echo off

if "%1" == "--gui" (
  start python .\gui.py
) else if "%1" == "--rconf" (
  start python .\reconfig.py
) else if "%1" == "--hahaThisParrotSecret" (
  curl parrot.live
) else if "%1" == "--help" (
  start https://github.com/josaih-mo/PyPaper/wiki
) else if "%1" == "--instant" (
  if "%2" == "" (
    echo Please provide a second parameter.
  ) else (
    start python .\instant.py %2
  )
) else (
  start python .\main.py
)
