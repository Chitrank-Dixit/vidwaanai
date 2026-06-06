# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Varaha Puran 0.1)
- **Original**: '1', .. " ""6. vftr ~~"'l ~ 3ftt '1', .. ,,41 ~ ftI''II.ijJ'GI .... e:(Ji~'M ~ If ~t<ft,,,, a .. 4Il ~ 111, ... , .... ""'" .,.;-..... {1M,' WI .. ".,R amt ~ .Qi'!h~"'" .. 41<11'4 .,,', • .;o; .. <11 .. ,~ ~, ",q .... ,d, ~ q , &.'&UI,<m" ~eiA'~'4" .It(ll;o411:,,,, .iftf'\ .... uf\f, _ ~nu ... "".Mt'.'1"'S , ''''~U' ill': , lit..! i "'\i'lfl:ot ........ , ... , i44ol4l~ .. ' &:gcd41 'Mil Ii if" If'ii!f{ l\'Ur, _ i'I,'Wf!:, lm'It • ~ ""~~k'I' 'I'mfI .. , ... <11 :on.: ~ i\"/£'I 'I'16l'\ .. "'~ ~~""I( ...w ~ ""!I'iI4'Ai, ~ ~ 34'11,"""., ~ VI'1I Wi1J"""~ ~~~!fd:';" ~ """"'1"" ~aft¥! qR ~ _ ~ 1(if:l 4> ...... 1:['RI 'Iltii '!JOI- '!JOI ~ 1ji((Ii t. T'4 'f'1IW!. M.~ ,4Ail( t, fl:R & .. IIi I 'I'm'\. ~ ('ll(lfl-'t lII'IR ¥R'I"I «'liftl ~, ..... ~'11111 ~ .,I';<lml\" '1 ... ''IlI ~ fImR:I ~ m .-ft ~ lIl1'I'l'I( P¥:?l" (@ -tll ~-MI~~ .... ~~'l{,_ N '(JIIUI ~ &~ _ :mil'" 'f""I 'l'I fII"1+Qil ~ ~ ~., &,,,*, 'mFt .... >W ri .. ,q,,", <*"", II'N, m-r _ &, ... ,11>0 ... l-'Iit 'I! ~, _ ~ t-tf .. ""if _ ""6111';, ~ "lIlq .. ~ l\'Ur-'I<'i ""'" ~ :IN-fI lifIDsm i(lfi,aj~ .. ' aA'lI ,*,,,[iIif f.!:n '1 ..... ,," = h, ;J(j "lr'I'I ~ '"' " .. """'" lqi' _ 9'iI, :RIll J4lQ; ~ ~ 34,I«;""if WI 'lI>m :m = ..mt ~';'ItJ~! ~-'!"i'lh ~ i1I.";:1 i! )<1"" .. "Il11T'i 'WCft 1 _
- **Translation**: 

---

