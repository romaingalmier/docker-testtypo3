
$password = ConvertTo-SecureString "!ysvLl?v5m" -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential ("storage", $password)
$Session =  New-SFTPSession -ComputerName server.snow-sftp.tx.group -Credential $Cred -AcceptKey -Verbose

$SessionId = $Session.SessionId

$pathFileToUpload = ".\" + $arg #TODO tester
$destinationFile = "/"#TODO tester

Set-SFTPItem -SessionId $SessionId -Destination $destinationFile -Path $pathFileToUpload -Force
Get-SFTPChildItem -SessionId $SessionId -Path ".."
#Write-Output($Session.SessionId)
Remove-SFTPSession -SessionId $SessionId -Verbose
