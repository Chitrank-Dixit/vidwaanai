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

### Verse 1 (Sama Ved 0.3341)
- **Original**: डति सप्तम: खण्ड:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3342)
- **Original**: उत्तार्चिके दशपो5 ध्याय: 10.7
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3343)
- **Original**: अष्टम: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3344)
- **Original**: 1304. अगन्म महा नमसा यविष्ठं यो दीदाय समिद्धः स्वे दुरोणे । चित्रभानुं रोदसी अन्तरुवीं स्वाहुतं विश्वतः प्रत्यक्षम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3345)
- **Original**: यज्ञ वेदिका में उत्तम रीति से प्रदीप्त, आकाश और पृथ्वी के मध्य, विशेषरूप से दीप्तिवान्‌, उत्तम आहुतियुक्त, सर्वत्रव्याप्त, चिर्युवा अग्निदेव को, हम श्रद्धापूर्वक नमन करते हुए, उनका आश्रय प्राप्त करते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3346)
- **Original**: 1305, स महा विश्वा दुरितानि साह्नानग्नि ष्टवे दम आ जातवेदा: । स नो रक्षिषदुरितादवद्यादस्मान्गूणत उत नो मघोनः
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3347)
- **Original**: अपने महान्‌ तेज से सब पापों को नष्ट करने वाले, ज्ञानरूपी प्रकाश के विस्तारक अग्निदेव, यज्ञशाला में प्रतिष्ठित होते हैं । वे स्तुत्य अग्निदेव हमें दोषपूर्ण एवं निन्दित कर्मों से बचाते हैं और आहुतियाँ स्वोकार करके हमारे योग-क्षेम का वहन करते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3348)
- **Original**: 1306. त्वं वरुण उत मित्रो अग्ने त्वां वर्धन्ति मतिभिर्वसिष्ठा: । त्वे वसु सुषणनानि सन्तु यूयं पात स्वस्तिभि: सदा न:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3349)
- **Original**: है अग्निदेव ! आप वरुण (कामनाओं को पूर्ति करने वाले) और मित्र (स्नेहपूर्वक सहयोग देने वाले) रूप हैं। विशिष्ट ऋषिगण श्रेष्ठ स्तुतियों से आपको गौरवान्वित करते हैं । आप श्रेष्ठ धन एवं कल्याणकारी साधनों से हमारी रक्षा करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3350)
- **Original**: 1307, महाँ इन्द्रो य ओजसा पर्जन्यो वृष्टिमाँ डब
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3351)
- **Original**: स्तोमैर्वत्सस्य वावृधे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3352)
- **Original**: वृष्टि करने वाले मेघों के सदूश महान्‌ और तेजस्वी वे इन्द्रदेव अपने प्रिय पात्रों की स्तुतियों से, व्यापकरूए ग्रहण कर यशस्वी होते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3353)
- **Original**: 1308. कण्वा इन्द्रं यदक्रत स्तोमैर्यज़्स्य साधनम्‌ । जामि ब्रुवत आयुधा
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3354)
- **Original**: जब कण्वादि ऋषिगण स्तुतियों के माध्यम से इन्द्रदेव को यज्ञसाधक (यज्ञरक्षक) बना लेते हैं, तो (यज्ञ रक्षार्थ) शख्त्रों की आवश्यकता नहीं रह जाती- ऐसा कहा गया है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3355)
- **Original**: 1309, प्रजामृतस्य पिप्रतः प्र यद्भरन्त वह्नय: । विप्रा ऋतस्य वाहसा
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3356)
- **Original**: । जब आकाश को घेर लेने वाली दिव्य अग्नियाँ यज्ञ के लिए तत्पर इद्धदेव को वेगपूर्वक (यज्ञस्थल पर) ले जाती हैं, तब उद्‌गातागण यज्ञीय स्तुतियों से उनकी स्तुति करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3357)
- **Original**: इति अष्टम:खण्ड
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3358)
- **Original**: नवम: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3359)
- **Original**: 1310. पवमानस्य जिघ्नतो हरेश्वन्द्रा असृक्षत । जीरा अजिरशोचिषः
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3360)
- **Original**: शत्रु-विनाशक, सर्वत्र गमनशौल तेज वाले हरिताभ सोमरस् की य/आह्वादकारी धारा, शोधित होकर प्रवाहित होती है
- **Translation**: 

---

