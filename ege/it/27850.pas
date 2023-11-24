Program TwoSevenEightFiveZero;
(* https://inf-ege.sdamgia.ru/problem?id=27850 *)
var
    count, numDel, i, j: longint;
begin
    count := 0;
    for i := 245690 to 245756 do begin
        count := count + 1;
        numDel := 2;
        for j := 2 to round(sqrt(i)) do begin
            if i mod j = 0 then begin
                numDel := numDel + 1;
                if numDel > 2 then break;
            end;
        end;
        if numDel = 2 then writeln(count, ' ', i);
    end;
end.
