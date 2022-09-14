.read data.sql


CREATE TABLE bluedog AS
  SELECT color,pet from students where color = "blue" and pet="dog";

CREATE TABLE bluedog_songs AS
  SELECT color,pet,song from students where color = "blue" and pet="dog";


CREATE TABLE smallest_int_having AS
  select time,smallest from students group by smallest having count(time) = 1;


CREATE TABLE matchmaker AS
select a.pet,a.song,a.color,b.color from students as a,students as b where a.pet = b.pet and a.song = b.song and a.time < b.time;
