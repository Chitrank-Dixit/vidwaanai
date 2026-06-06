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

### Verse 1 (Vishnu Puran 0.11221)
- **Original**: ये सोत्कह हजार एक सौ ख्तरियाँ थीं; उन सबके साथ पाणिग्रहण करते समय श्रीमधुसूदनने इतने ही रूप बना लिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11222)
- **Original**: हे मैप्रेय ! परेतु उस समय प्रत्येक कत्या 'भगवानने मेरा ही पाणिग्रहण किया है' इस प्रकार उन्हें एक ही समझ रही थी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11223)
- **Original**: हे चिप्र ! जगत्सष्टा विश्वरूपघारी श्रीहरि राज़िकि समय उन सभीके घरोंमें रहते थे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11224)
- **Original**: कज है 3 क--ज+ इति श्रीविष्णुपुराणे पञ्ममेंडशे एकत्रिशोउघध्याय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11225)
- **Original**: 00007 जद पतन बत्तीसवाँ अध्याय उषा-चकरित्र श्रीपराद्वर उवाच प्रह्युम्नाद्या हरे: पुत्रा रुक्मिण्यां कथ्चितास्तव । भानुभौमेरिकाद्यांश्र सत्यभामा व्यजायत
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11226)
- **Original**: 91 दीप्विमत्ताग्रपक्षाद्या रोहिण्यां तनया हरे: । बभूवुर्जाम्बव॒त्यां च साम्बाद्या बलझालिन:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11227)
- **Original**: 2 तनया भद्गविन्दाद्या नाप्रजित्यां महावला: । सद्ष्यामजित्रधानास्तु शैव्यायां च हरेस्सुता:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11228)
- **Original**: 3 बृकाद्याअ सुता माद्रयां गात्रवठ्ामुखान्सुतान्‌ । अवाप लक्ष्मणा पुत्रान्कालिन्धाअ श्रुतादय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11229)
- **Original**: 4 अन्यासां चैब भार्याणां समुत्पन्नानि चक्रिण: । अष्टायुतानि पुत्राणां सहस्नाणि झतं तथा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11230)
- **Original**: 5 श्रीपराह्रजी खोले--रुक्मिणीके गर्भसे उत्पन्न हुए. भगवानके प्रधुम्त आदि पुत्रोंका वर्णन हम पहले ही कर चुके हैं; सत्यभामाने भानु और भौमेरिंक आदिको जन्म दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11231)
- **Original**: श्रीहरिके रोहिणोंके गर्भसे दीप्तिमान्‌ और ताम्रपक्ष आदि तथा जाम्बबतीसे बलदाली साम्ब आदि पुत्र हुए
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11232)
- **Original**: नात्रजिती (सत्या) से महाबली भद्ग॒विन्ट आदि ओर जैव्या (मित्रविन्दा) से संप्रामजित्‌ आंदि उत्पन्न हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11233)
- **Original**: मादीसे वृक आदि, लक्ष्मणासे गात्रवान्‌ आदि तथा कालिन्दीसे श्रुत आदि पुत्रोंका जन्प हुआ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11234)
- **Original**: इसी प्रकार भगवानकी अन्य स्क्त्योंके भी आठ अयुत आठ हजार आठ सौ (अड्टासी हजार आठ सौ) पुत्र हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11235)
- **Original**: 396 प्रद्मुम्न: प्रथमस्तेषां सर्वेषां रुक्मिणीसुतः । प्रद्मूप्नादनिरुद्धोउभूहज़स्तस्मादजायत._
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11236)
- **Original**: 6 अनिरुद्धो रणेःरुद्धो बले: पोत्रीं महाब॒त्ठः । उषां बाणस्थ तनयामुप्येमे द्विजोत्तम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11237)
- **Original**: 7 यत्र युद्धमभूद्वोरं हरिशद्भरयोर्महत्‌ । छिन्न॑ सहस्त्नं बाहूनां यत्र बाणस्य चक्रिणा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11238)
- **Original**: 8 श्रोमैत्रेय उताच कथ्थ॑ युद्धमभूदब्हामन्ुषार्थें हरकृष्णयो: । कर्थ क्षयं च बराणस्य बाहूनां कृतवान्हरि:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11239)
- **Original**: 9 एतत्सर्व महाभाग ममाख्यातुं त्वमहसि। महत्कौतूहलं जात॑ कथां ओ्रोतुमिमां हरे:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11240)
- **Original**: 10 ओपराशर उवाच उषा बाणसुता विप्र पार्वती सह झम्भुना
- **Translation**: 

---

