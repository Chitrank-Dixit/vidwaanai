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

### Verse 1 (Vishnu Puran 0.6361)
- **Original**: सृक्षयात्सहदेव:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6362)
- **Original**: ततश्र कुशाश्रो नाम पुन्नोईभवत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6363)
- **Original**: सोमदत्त: कृशाश्चवाजज्ञे योअश्वमेधानां झतमाजहार
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6364)
- **Original**: तत्पुन्रो जनमेजयः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6365)
- **Original**: जनमेजयात्सुमति:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6366)
- **Original**: _ एते वैशालिका भूभृतः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6367)
- **Original**: इलोकोउप्यत्र गीयते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6368)
- **Original**: तृणबिन्दो: प्रसादेन सर्वे वैशात्क्का नृपाः । दीर्घायुषो महात्मानो बीर्यवन्तोःतिधार्मिकाः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6369)
- **Original**: 69 शार्याते: कन्या सुकन्या नामाभवत्‌ य़ामुपयेमे चख्यवन:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6370)
- **Original**: 62 । आनर्त्तनामा परमथार्मिक- इशर्यातिपुत्रो5भवत्‌ ।। 63
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6371)
- **Original**: . आनर्त्तस्यापि रेबतनामा पुत्रो यज्ञे योउसावानर्त्तविषयं बुभुजे पुरी च कुशस्थलीमध्युबास
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6372)
- **Original**: रेबतस्थापि रैजतः पुत्र: ककुब्मिनामा धर्मात्मा भ्रातृशतस्य ज्येप्ठो3भवत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6373)
- **Original**: तस्य रेवती नाम कन्याभवत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6374)
- **Original**: स॒तामादाय कस्येय- महतीति भगवन्तमब्जयोनि प्रष्ठे ब्रहालोके जगाम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6375)
- **Original**: तावथ् ब्रह्मणोउन्तिके हाहाहूहुसंज्ञाभ्यां गन्धर्वाभ्यामतितानं नाम दिव्यं गान्धर्बभगीयत गीतावसाने च भगवन्तमब्जयोनि प्रणम्य रैवत: चतुर्थ अंश र29 केयल और केखलसे सुधृतिका जन्म हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6376)
- **Original**: सुधृतिसे नर, नरसे चन्द्र और चन्द्रसे केवल हुआ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6377)
- **Original**: केशलसे बन्धुमान्‌, बन्खुसानसे वेगवान्‌, वेगवानसे बुध, बुधसे ठृणबिन्दु तथा तृणबिन्दुसे पहले तो इलबिला नामकी एक कन्या हुई थी, किन्तु पीछे अल्च्बुसा नामकी एक सुन्दरी अप्सरा उसपर अनुरक्त हो गयो । उससे तृणबिन्दुके विज्ञाऊ नामक पुत्र हुआ, जिसने विशाल्म नामकी पुरी बसायी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6378)
- **Original**: 43--49
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6379)
- **Original**: विशालका पुत्र ब्रेमचद हुआ, हेसचद्रका चद्, चऋन्द्रका धूप्राश्, धूप्राक्षक्र सूुझ्य, सुझ्यका सहदेव और सहदेवका पुत्र क॒शाश्व हुआ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6380)
- **Original**: 50--55
- **Translation**: 

---

