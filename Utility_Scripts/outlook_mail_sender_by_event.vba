Public WithEvents objReminders As Outlook.Reminders

Const EmailSubject_1 = "Event1"
Const EmailSubject_2 = "Event2"

Private Sub Application_Startup()
  Set objReminders = Application.Reminders
End Sub

Private Sub objReminders_ReminderFire(ByVal ReminderObject As Reminder)
If ReminderObject.IsVisible = True Then
  Dim objMI As Outlook.MailItem
  If ReminderObject.Item.Subject = EmailSubject_1 Then

    Set objMI = Application.CreateItem(olMailItem)
    With objMI

      .Subject = EmailSubject_1
      .SentOnBehalfOfName = ".....com"
      .To = "....com"
      .CC = "....com;.....com"
      .HTMLBody = "<HTML><BODY><p>Buon pomeriggio,<br>Testo corpo.<br><br>A disposizione,<br>Saluti<br></p></HTML></BODY>"
      .Attachments.Add "path all'allegato"
      .Send

    End With

    ''ReminderObject.Dismiss

    Set objMI = Nothing

  End If

  If ReminderObject.Item.Subject = EmailSubject_2 Then
    Set objMI = Application.CreateItem(olMailItem)
    With objMI

      .Subject = EmailSubject_2
      .SentOnBehalfOfName = "....com"
      .To = "....com"
      .CC = "....com;....com"
      .HTMLBody = "<HTML><BODY><p>Buon pomeriggio,<br>itesto corpo.<br><br>A disposizione,<br>Saluti<br></p></HTML></BODY>"
      .Attachments.Add "path all'allegato"
      .Send

  End With

    ''ReminderObject.Dismiss

    Set objMI = Nothing
  End If



  If ReminderObject.Item.Subject = EmailSubject_2 Or ReminderObject.Item.Subject = EmailSubject_1 Then
    ReminderObject.Item.Delete
  End If



End If

''GET ALL SYNC GROUPS
''Set mySyncObjects = OutApp.GetNamespace("MAPI").SyncObjects

''KICK OFF SYNC FOR ITEM 1 IN SYNC GROUPS, USUALLY ALL ACCOUNTS - MAY NEED TO LOOP THROUGH ALL SYNC GROUPS TO FIND "ALL ACCOUNTS"
''mySyncObjects(1).Start

End Sub
