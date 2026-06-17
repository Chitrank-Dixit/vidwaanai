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

### Verse 1 (Vishnu Puran 0.7821)
- **Original**: इसलिये तुम दूसरेकी शरण स्ते' अक्ररके ऐसा कहनेपर शतधन्वाने कहा---
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7822)
- **Original**: 'अचछ, यदि पेशी रक्षा करनेयें आप अपनेक्त सर्वथा असमर्थ समझते हैं तो मैं आपको यह मणि देता हूँ इसे लेकर इसीकी रक्षा क्यैजिये'
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7823)
- **Original**: इसपर अक्रूरने कहा--
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7824)
- **Original**: “मैं इसे तभी ले सकता हूँ जब कि अन्तकाल उपस्थित होनेपर भी तुम किसीसे भी यह बात न कहो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7825)
- **Original**: झतथन्‍्वाने कह्ला-- ऐसा ही होगा ।" इसपर अक्रूरने बह मणिरत्र अपने पास रख लिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7826)
- **Original**: तदनन्तर, शतधन्बा सौ योजनतक जानेबाली एक अत्यन्त बरेगबतों घोड़ोपर चढ़कर भागा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7827)
- **Original**: और जैन्य, सुओऔन, गेघपुष्प तथा बल्ाहक नामक चार चघोड़ोंवाले रथपर चढ़कर बल्दरेज और वासूदेयने भी उसका पीछा क्रिया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7828)
- **Original**: सौ योजन मार्ग पार कर जानेपर पूनः आगे ले जानेसे उस घोड़ीने मिथिला देशफे वनमें प्राण छोड़ दिये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7829)
- **Original**: तब शतथधन्वा उसे खेड़कर पैदल हो भागा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7830)
- **Original**: उस समय अश्रीकृष्णचद्धने बलछूभद्रजी से कहा--
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7831)
- **Original**: 'आप अभो रथमें ही रहिये मैं इस पैदल दौड़ते हुए दुगचारीको पैदक जाकर ही भोरे डाख्य्ता हूँ। यहाँ [
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7832)
- **Original**: घोड़ीके मरने आदि ] दोषोंको देखनेसे घोडे भयभीत हो रहे हैं, इसलिये आप इन्हें और आगे न बढ़ाइयेगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7833)
- **Original**: तब बल्देवजी 'अच्छा' ऐसा कहकर रथमें ही बैठे रहे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7834)
- **Original**: श्रीकृष्णचद्धने केवल दो हो कोसतक पीछाकर अपना चक्र. फेंक दूर होनेपर भी शतधन्वाका सिर काट डाला
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7835)
- **Original**: कितु उसके दारीर और वस्त्र आदियें बहुत कुछ ढूँढ़नेपर भी जब स्यमन्तकम्णिकों न पाया तो बलभद्रजीके पास जाकर उनसे कहा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7836)
- **Original**: “हमने शतधन्वाको व्यर्थ ही मारा, क्योंकि उसके पास सम्पूर्ण संसास्की सारभूत स्पमन्‍तकमणि तो मिल्णी ही नहीं।' यह सुनकर बलदेवजीने [ यह समझकर कि श्रीकृष्णचन्द्र उस मणिकों छिपानेके छिये ही ऐसी बातें बना रहे-हैं.
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7837)
- **Original**: अ0 93 ) खासुदेवमाह
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7838)
- **Original**: धिक्त्वां यस्त्वमेवमर्थ- लिप्सुरेतच्व॒ते प्रातृत्वान्मया क्षान्ते तदय॑ पन्धास्स्वेच्छया गम्यतां न में द्वारकया न त्वया न सानोषपि न तस्थौ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7839)
- **Original**: स विदेहपुरी प्रवियेश
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7840)
- **Original**: जनकराजश्चार्ध्यपूर्वकमेन॑ गृह प्रवेशयामास
- **Translation**: 

---

