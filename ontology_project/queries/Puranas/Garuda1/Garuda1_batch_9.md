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

### Verse 1 (Garuda1 0.161)
- **Original**: कुबेरस्थ पतिश्व नक्षत्राणां. पतिस्तथा। ओपषधीना पतिक्षेवयव॒क्षाणां च पततिस्तथा
- **Translation**: 

---

### Verse 2 (Garuda1 0.162)
- **Original**: नागानां पतिरकंस्थ दक्षस्थ पतिव ऊना सुददां च पतिक्षेत् नृपाणां अ्र॒ पतिस्तथा
- **Translation**: 

---

### Verse 3 (Garuda1 0.163)
- **Original**: पर्वतानां. पतिश्षैव निम्नगानां. पतिस्तथा
- **Translation**: 

---

### Verse 4 (Garuda1 0.164)
- **Original**: सुराणां लव पति: श्रेष्ठ: कपिलस्य पतिस्तथा। सतानां च॑ पतिश्षेण बीरुधां च पतिस्तथा
- **Translation**: 

---

### Verse 5 (Garuda1 0.165)
- **Original**: । पतिक्षद्रमस: श्रेष्ठ; शुक्रस्थ पतिरेय. ज
- **Translation**: 

---

### Verse 6 (Garuda1 0.166)
- **Original**: ग्रहाणां क्ष॒ पतिश्षेैव राक्षसानां . पतिस्तशथा। किन्तराणां. पतिझव द्विजाना. पतिरुत्तम:
- **Translation**: 

---

### Verse 7 (Garuda1 0.167)
- **Original**: सरिता. ख॑ पतिश्लैव समुद्राणां. पतिस्तथा। सरसां च ( रसानां च्ञ ) पतिश्ैस भूतानां चर पतिस्तथा
- **Translation**: 

---

### Verse 8 (Garuda1 0.168)
- **Original**: वेतालानां पतिशव कृष्पाण्डानां. पतिस्तथा। पक्षिणां च पति: श्रेष्ठ: पशूनां पतिरिव च
- **Translation**: 

---

### Verse 9 (Garuda1 0.169)
- **Original**: आ मेरुमाता प्रधाणं ह् माधवो मलवर्जित:
- **Translation**: 

---

### Verse 10 (Garuda1 0.170)
- **Original**: महाशाज्रों महाभागो मथुसूदत एव च
- **Translation**: 

---

### Verse 11 (Garuda1 0.171)
- **Original**: महावीयों.. महाप्राणों. सार्कण्डेयर्षिवन्दित:। मायात्मा मायया बरद्धाों मायया तु खिवर्जित:
- **Translation**: 

---

### Verse 12 (Garuda1 0.172)
- **Original**: सुनिस्तुतो मुनिर्षैत्रो महाना (रा) सो महाहनु:। महाबाहुर्महादान्तो ( महादन्तों) मरणेन विवर्जित:
- **Translation**: 

---

### Verse 13 (Garuda1 0.173)
- **Original**: महावक्‍्त्रों महात्मा चर महाकायो महोदर:। महापादों महाग्रीवों महासातवी महामनाः
- **Translation**: 

---

### Verse 14 (Garuda1 0.174)
- **Original**: महागतिर्महाकीरतिर्महारूपो महासुर:। मधुश्ष माशवज्शैब पहादेवो. पहेश्वर:
- **Translation**: 

---

### Verse 15 (Garuda1 0.175)
- **Original**: मखेज्यो घखरूपी लव माननीयों मसेश्रः ( महेश्वर: )। महाथातो महाभागो.. सहेशोउतीतमानुष:
- **Translation**: 

---

### Verse 16 (Garuda1 0.176)
- **Original**: मसानवशभ्ञ पमनुझैथव मानवानां. प्रियडूरः। समृगक्ष मृगपूज्यक्ष समृगाणां उल॑ ृपतिस्तथा
- **Translation**: 

---

### Verse 17 (Garuda1 0.177)
- **Original**: लक्ष्मणो लक्षणज्षव खम्बीधह्लों. ललितस्तथा। नानालझ्लनरसंयुक्तो नानाचन्दनचर्सित:
- **Translation**: 

---

### Verse 18 (Garuda1 0.178)
- **Original**: जानारसोज््वलट्टयत्रो जानापुष्पोपशोभित: । रामों. रमापतिक्षक सभार्य:. परमैक्षरं:
- **Translation**: 

---

### Verse 19 (Garuda1 0.179)
- **Original**: रलदो रतह॒ता ज्ञ॒ रूपी रूपविवर्जित:। महारूपोग्ररूपक्ष सौप्यरूपस्तलैय चाआ नीलमेघनिभ: शुद्ध: कालमेघनिभस्तथा। धूमवर्ण: पीतवर्णों नानारूषो ( नानावर्णो ) ह्ावर्णक:
- **Translation**: 

---

### Verse 20 (Garuda1 0.180)
- **Original**: विरूपो.. कृपदक्षण शुक्लवर्णस्तथेव था सर्ववर्णों महायोगी यज्ञो ( याज्यो ) यज़्कृदेव चा
- **Translation**: 

---

