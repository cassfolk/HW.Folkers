Sub VBAHW_FinalRun():

Dim Sheet As Worksheet

    For Each Sheet In Worksheets
        'do for each sheet really mean it kthanksbye
        Sheet.Select
        
        lastrow = Cells(Rows.Count, 1).End(xlUp).Row
        lastrowPerC = Cells(Rows.Count, "K").End(xlUp).Row
        lastrowTicker = Cells(Rows.Count, "I").End(xlUp).Row

        Dim ticker As String
        Dim TotalStock As Double

        Dim YearlyC As Double
        Dim PerC As Double
        Dim Open_ As Double
        Dim Close_ As Double
        Dim Change As Double

        'Set table for results of Instructions (see readme on HW)
        Dim SumTable As Integer
        SumTable = 2

        'Set words in cells
        Cells(1, 9).Value = "Ticker"
        Cells(1, 10).Value = "Yearly Change"
        Cells(1, 11).Value = "Percent Change"
        Cells(1, 12).Value = "Total Stock Value"

        Cells(1, 16).Value = "Ticker"
        Cells(1, 17).Value = "Value"
        Cells(2, 15).Value = "Greatest % Increase"
        Cells(3, 15).Value = "Greatest % Decrease"
        Cells(4, 15).Value = "Greatest Total Value"


        'STUPID THING - makes it so divide by zero has a reference to NOT divide by zero. Needed to be BEFORE (not in) 2nd if statment
        For i = 2 To lastrow
            If Open_ = 0 Then
                Open_ = Cells(i, 3).Value
            End If
            
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                ticker = Cells(i, 1).Value
                Close_ = Cells(i, 6).Value
              
                YearlyC = Close_ - Open_
                
                    'Error 11 - DIVIDE BY ZERO ERROR GRRRRRRRRRRR
                    'Tried CLing() around both parts of PerC
                    'Tried If for Open_ = 0 then Open_Cells.value
                    'Tried If YearlyC / Open_ = 0 then PerC 0
                    '****FIXED -- added in the if Open_ = 0 statement at top in addtion to statement below
                    If Open_ <> 0 Then
                         'looked up math formula for percentage and used Close_ - Open_ / Open_ ....already had YearlyC as top part
                        PerC = YearlyC / Open_
                    Else
                        PerC = 0
                    End If

                'Tell them where to stick it (what above goes where in table)
                Range("I" & SumTable).Value = ticker
                Range("L" & SumTable).Value = TotalStock
                Range("J" & SumTable).Value = YearlyC
                Range("K" & SumTable).Value = PerC

                'set as %
                Range("K" & SumTable).NumberFormat = "0.00%"
                Cells(i, 11).NumberFormat = "0.00%"
                
                'have sumtable built/down 1 row per ticker
                SumTable = SumTable + 1

                'why in if = reusing in each ticker = RESET
                TotalStock = 0
                Close_ = 0
                Open_ = 0
            
            'else = if SAME sum TotalStock
            Else
                'Adds up all same cause not different
                TotalStock = TotalStock + Cells(i, 7).Value
                
            End If


            'ALL THE COLORS
            If Cells(i, 10).Value > 0 Then
                Cells(i, 10).Interior.ColorIndex = 4
                ElseIf Cells(i, 10).Value < 0 Then
                    Cells(i, 10).Interior.ColorIndex = 3
                Else
                    Cells(i, 10).Interior.ColorIndex = 0
            End If

        Next i
        
        'Ticker was hard to figure out -- yay learning how to use WorksheetFunctions...index,match,max/min = worked...vlookup,offset did not)

        'Find max
        Range("Q2").Value = WorksheetFunction.Max(Range("K:K"))
        'Find max ticker
        Range("P2").Value = WorksheetFunction.Index(Range("I:I"), WorksheetFunction.Match(WorksheetFunction.Max(Range("K:K")), Range("K:K"), 0))
        
        'Find min
        Range("Q3").Value = WorksheetFunction.Min(Range("K:K"))
        'Find min ticker
        Range("P3").Value = WorksheetFunction.Index(Range("I:I"), WorksheetFunction.Match(WorksheetFunction.Min(Range("K:K")), Range("K:K"), 0))

        'Find gresatest Stock
        Range("Q4").Value = WorksheetFunction.Max(Range("L:L"))
        'Find gresatest Stock ticker
        Range("P4").Value = WorksheetFunction.Index(Range("I:I"), WorksheetFunction.Match(WorksheetFunction.Max(Range("L:L")), Range("L:L"), 0))


        'Set Max/Min as %
        Range("Q2:Q3").NumberFormat = "0.00%"

    Next

End Sub

