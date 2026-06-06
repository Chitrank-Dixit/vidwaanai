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

### Verse 1 (Sama Ved 0.3201)
- **Original**: 1242, शुक्र: पवस्व देवेभ्य: सोम दिवे पृथिव्य शं च प्रजाभ्य:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3202)
- **Original**: है कान्तिमान्‌ सोमदेव ! आप दिव्य गुणों के लिए प्रवाहित हों । आकाश, पृथ्वी तथा प्रजाओं (समस्त जीव- जगत्‌) को सुख प्राप्त हो
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3203)
- **Original**: 9.10 सामवेद-संहिता 1252. इन्द्रमीशानमोजसाभि स्तोमैरनूषत । सहस्न॑ यस्य रातय उत वा सन्ति भूयसी:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3204)
- **Original**: उद्‌गातागण असंख्यों अनुदान देने वाले, सामथ्यों के स्वामी इन्द्रदेव की स्तुति करने लगे
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3205)
- **Original**: इति नवमः खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3206)
- **Original**: ऋषि, देवता, छन्द-विवरण ऋषि--प्रतर्टन दैवोदासि 11575-1177
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3207)
- **Original**: असित काश्यप अथवा देवल 1178-1204
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3208)
- **Original**: उचथ्य आज्रिरस्स 1205-1209, 1225-1227। अमहीयु आद्लिरस 1210-1215। निधुवि काश्यप 1216-1218, 1235-1237 । वसिष्ठ मैत्रावरण 1219-1221
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3209)
- **Original**: सुकक्ष आद्रिसस 1222-1224
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3210)
- **Original**: कवि भार्गव 1228-1230 । देवातिथि काण्व 1231-1232 । भर्ग प्रागाथ 1233-1234 । अम्बरीष वार्षागिर और ऋजिश्चा भारदाज 1238-1240 ।अग्नि धि7ष्ण्य ऐश्वर 1241-1243
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3211)
- **Original**: उशना काव्य 1244-1246 । नृमेध आड्रिस 1247-1249 । जेता माधुच्छन्दस 1250-1252 । देवता-पवमान सोम 1175-1218, 1225-1230, 1235-1243
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3212)
- **Original**: अग्नि 1219-1221, 1244-1246 । इन्र 1222-1224, 1231-1234, 1247-1252 । छन्द-व्रिष्प. 1175-1177, 1219-1221। गायत्री 1178-1218, 1222-1227, 1235-1237, 1244-1246
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3213)
- **Original**: जगती 1228-1230 । बार्हत प्रगाथ (विषमा बृहती, समा सतोवृहती) 1231-1234 । अनुष्टप्‌ 1238-1240, 1250-1252 । द्विपदा विराट गायत्री 1241-1243 । उष्णिक्‌ 1247-1249 ।
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3214)
- **Original**: इति नवमो5 ध्याय:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3215)
- **Original**: -+ा<ी.जलवल-न्‍नत20-छ--+..*
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3216)
- **Original**: अथ दश्मो5 ध्याय: ।।
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3217)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3218)
- **Original**: 1253. अक्रान्त्समुद्र प्रथमे विधर्मन्‌ जनयन्ग्रजा भुवनस्य गोपा: । बृषा पवित्रे अधि सानो अव्ये बृहत्सोमो वावृथे स्वानो अद्रिः
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3219)
- **Original**: जल की वृष्टि करने वाला , सर्वरक्षक दिव्यसोम, विस्तृत आकाश में सर्वप्रथम प्रजाओं की उत्पत्ति करके श्रेष्ठतम महत्त्व को प्राप्त हुआ, तदनन्तर पृथ्वी के ऊपर स्थापित प्राकृतिक शोधक (छन्‍्ने) के द्वारा प्रवेश करता हुआ वृद्धि को प्राप्त होता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3220)
- **Original**: रू 1254. मत्सि वायुमिष्टये राधसे नो मत्सि मित्रावरुणा पूयमान: । मत्सि शर्थों मारुतं मत्सि देवान्मत्सि द्यावापृधिवी देव सोम
- **Translation**: 

---

