drop table if exists csdn_java_content;
create table csdn_java_content (
	content_id int not null auto_increment,
	content_url char(200) not null,
	content_fn char(200) not null,
	title char(100),
	author char(30),
	group_name char(30),
	primary key (content_id)
)engine = innodb;
create index idx_title on csdn_java_content(title);