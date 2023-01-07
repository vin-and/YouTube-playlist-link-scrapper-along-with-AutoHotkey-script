Sleep 1000
Loop, read, links.txt
{
Loop, parse, A_LoopReadLine, %A_Tab%
{
Send %A_LoopReadLine%{tab}{enter}
Sleep 500
Send {enter}
Sleep 500
}
}