program BeautifulMatrix;

var
  coord_x, coord_y, line_number: Integer;
  line: String;
begin
  coord_x := 0;
  coord_y := 0;
  for line_number := 1 to 5 do
  begin
    Readln(line);
    if Pos('1', line) = 0 then
      Continue;
    coord_y := line_number;
    coord_x := ((Pos('1', line) - 1) div 2) + 1;
    Break;
  end;
  WriteLn(Abs(3 - coord_x) + Abs(3 - coord_y));
end.

