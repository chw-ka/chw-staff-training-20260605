Attribute VB_Name = "GenerateWenYanWenSlides"
Option Explicit

' 中一中文科：文言文基本閱讀技巧（六書與虛詞）
' 10 slides — Office 365 compatible, no external references
' Run: Alt+F11 → Insert Module → paste → F5

Public Sub GenerateWenYanWenSlides()
    Dim oPres As Presentation
    Dim oSlide As Slide
    Dim oTitle As Shape
    Dim oBody As Shape
    Dim oText As TextRange

    On Error GoTo ErrHandler

    Set oPres = Application.Presentations.Add(msoTrue)

    Do While oPres.Slides.Count > 0
        oPres.Slides(1).Delete
    Loop

    ' Slide 1 — Title
    Set oSlide = oPres.Slides.Add(1, ppLayoutTitle)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "中一中文科"
    oBody.TextFrame.TextRange.Text = "文言文基本閱讀技巧" & vbCrLf & "六書與虛詞"

    ' Slide 2 — 課程目標
    Set oSlide = oPres.Slides.Add(2, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "課程目標"
    oBody.TextFrame.TextRange.Text = _
        "• 認識文言文的特點" & vbCrLf & _
        "• 了解「六書」造字法" & vbCrLf & _
        "• 辨識常見虛詞的語氣與功能" & vbCrLf & _
        "• 能運用基本技巧閱讀簡短文言文"

    ' Slide 3 — 什麼是文言文
    Set oSlide = oPres.Slides.Add(3, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "什麼是文言文？"
    oBody.TextFrame.TextRange.Text = _
        "• 古代漢語書面語，與現代白話不同" & vbCrLf & _
        "• 字數精簡，一字多義" & vbCrLf & _
        "• 常見於經史子集、古典文學" & vbCrLf & _
        "• 例子：「學而時習之，不亦說乎？」"

    ' Slide 4 — 六書概覽
    Set oSlide = oPres.Slides.Add(4, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "六書概覽"
    oBody.TextFrame.TextRange.Text = _
        "象形 — 描繪物形" & vbCrLf & _
        "指事 — 以符號示意" & vbCrLf & _
        "會意 — 合兩意成新意" & vbCrLf & _
        "形聲 — 形旁 + 聲旁" & vbCrLf & _
        "轉注 — 同義互訓（進階）" & vbCrLf & _
        "假借 — 借音表意（進階）"

    ' Slide 5 — 象形
    Set oSlide = oPres.Slides.Add(5, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "象形"
    oBody.TextFrame.TextRange.Text = _
        "直接描繪事物外形" & vbCrLf & vbCrLf & _
        "例字：日、月、山、水" & vbCrLf & _
        "教學提示：請學生畫出字與物的對應"

    ' Slide 6 — 指事
    Set oSlide = oPres.Slides.Add(6, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "指事"
    oBody.TextFrame.TextRange.Text = _
        "以抽象符號指示位置或性質" & vbCrLf & vbCrLf & _
        "例字：上、下、本（木之根）" & vbCrLf & _
        "教學提示：對比「本」與「末」"

    ' Slide 7 — 會意
    Set oSlide = oPres.Slides.Add(7, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "會意"
    oBody.TextFrame.TextRange.Text = _
        "兩個或以上部件合併表達新意" & vbCrLf & vbCrLf & _
        "例字：明（日月）、休（人倚木）" & vbCrLf & _
        "教學提示：拆解部件討論字義"

    ' Slide 8 — 形聲
    Set oSlide = oPres.Slides.Add(8, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "形聲"
    oBody.TextFrame.TextRange.Text = _
        "形旁表義類，聲旁表讀音" & vbCrLf & vbCrLf & _
        "例字：河（水 + 可）、情（心 + 青）" & vbCrLf & _
        "教學提示：形聲字佔漢字大多數"

    ' Slide 9 — 虛詞
    Set oSlide = oPres.Slides.Add(9, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "虛詞簡介"
    oBody.TextFrame.TextRange.Text = _
        "虛詞：沒有實義，表語氣、結構或關係" & vbCrLf & vbCrLf & _
        "之 — 的 / 取消句子独立性" & vbCrLf & _
        "其 — 他的 / 那" & vbCrLf & _
        "者 — ……的人 / 事物" & vbCrLf & _
        "也 — 句末語氣（表判斷、停頓）" & vbCrLf & _
        "乎 / 哉 — 疑問或感嘆"

    ' Slide 10 — 小測與總結
    Set oSlide = oPres.Slides.Add(10, ppLayoutText)
    Set oTitle = oSlide.Shapes.Title
    Set oBody = oSlide.Shapes.Placeholders(2)
    oTitle.TextFrame.TextRange.Text = "小測與總結"
    oBody.TextFrame.TextRange.Text = _
        "小測：" & vbCrLf & _
        "1. 「休」屬哪一種造字法？" & vbCrLf & _
        "2. 「學而時習之」的「之」作何解？" & vbCrLf & vbCrLf & _
        "總結：先辨造字，再讀虛詞，循序漸進"

    ' Uniform font sizing
    Dim s As Slide
    Dim sh As Shape
    For Each s In oPres.Slides
        For Each sh In s.Shapes
            If sh.HasTextFrame Then
                If sh.TextFrame.HasText Then
                    Set oText = sh.TextFrame.TextRange
                    oText.Font.Name = "Microsoft JhengHei"
                    If sh.Type = msoPlaceholder Then
                        If sh.PlaceholderFormat.Type = ppPlaceholderTitle Then
                            oText.Font.Size = 36
                        Else
                            oText.Font.Size = 24
                        End If
                    Else
                        oText.Font.Size = 24
                    End If
                End If
            End If
        Next sh
    Next s

    oPres.SlideShowSettings.StartingSlide = 1
    oPres.SlideShowSettings.EndSlide = 10

    MsgBox "完成！已建立 10 張簡報：" & vbCrLf & oPres.Name, vbInformation, "文言文簡報產生器"
    Exit Sub

ErrHandler:
    MsgBox "執行時發生錯誤：" & Err.Description, vbCritical, "文言文簡報產生器"
End Sub
