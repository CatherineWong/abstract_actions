/*
 * SQL for querying a CHILDES-db instance
 */
select t.id, t.gloss, substring_index(t.stem, '-', 1), t.relation, t.speaker_code, t.target_child_id, t.target_child_age
from token as t
where t.part_of_speech = 'v' and t.speaker_code != 'CHI' and t.target_child_age > 1 * 365 and t.target_child_age < 3 * 365;
