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

### Verse 1 (Vishnu Puran 0.141)
- **Original**: 41 सप्मन्ति ततोअभांसि रसाथाराणि तानि च रसमात्राणि चाम्म्रांसि रूपमात्र समाबृणोत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.142)
- **Original**: 42 बिकुर्वाणानि चाम्भांसि गन्धमात्र॑ ससर्जिरे । सल्बातो जायते तस्मात्तस्थ गन्धो गुणो मत:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.143)
- **Original**: 43 तस्सिंस्तसिसिस्तु तन्मात्र तेन तन्पात्रता स्मृता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.144)
- **Original**: डंडे त्त्पात्राण्यविशेषाणि अविश्ेयास्ततो हि ते
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.145)
- **Original**: 45 न ज्ञान्ता नापि घोरास्ते न मूढाश्राविशेषिण; । भूततन्पात्रसगोडयमहल्लारातु तापसात्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.146)
- **Original**: 465 तैजसानीन्द्रियाण्याहूर्देवा वैकारिका दशा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.147)
- **Original**: एकादर्श मनश्षात्र देवा चैकारिका: स्पृता:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.148)
- **Original**: 47 विष्णु ही समष्टि-व्यप्टिरूप, ब्रह्मादि जीवरूप तथा महत्तत्त्वरूपसे स्थित हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.149)
- **Original**: है द्विजश्रेष्त ! सर्गकाकके प्राप्त होनेपर शुणोंक्रौ साम्गावस्थारूप अधान जय थिष्णुके क्षेत्रज्ञरूपसे अधिए्रित हुआ ते उससे महत्त्तवकी उत्पत्ति हुईं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.150)
- **Original**: उत्पन्न हुए प्रह्मस॒क्कों प्रधानतत्तने आयुत किया; महत्तत्त्व सात्विक, राजस और तापस, भेदसे तौन प्रक्तारका है। किन्तु जिस च्रकार बीज छिलकेेसे समभावसे ढेक्य रहता है लेसे ही यह व्रिजिध महत्तत्त्व प्रधान-तलसे रूख ओर व्याप्त है। फिरें त्रिनिध महतत्वसे ही सैकारिक (सात्तककि) तेजस (राज़स) और त़ामस्र भूतादि तीन प्रकारका अहंकार उत्पन्न हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.151)
- **Original**: है महामुने ! यह तिगुणात्यक होनेसे भूत और इच्द्रिय आदिका कारण है और प्रधानसे जैसे महत्तत्त व्या। ऐ, जैसे ही महत्तखसे बह (अहंकार) व्याप्त है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.152)
- **Original**: 34 --36
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.153)
- **Original**: भूतादि नाप्ृक खामस अहंकारने लिकृत होकर झाब्द-तन्मात्रा और उससे दाव्द-गुणवाले साकात्ञाकों रचना की
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.154)
- **Original**: डस धूतादि तापस अहंकारने दन्द-तन्पात्रारूप आकाशको व्याप्त किया। फिर [शब्द-तन्मात्रारूप) आकाशने बिकृते होकर स्पर्वा-तन्मात्राकों रचा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.155)
- **Original**: उस (स्पर्श-तमात्रा) से बलबान्‌ यायु हुआ.डसका गुण स्पर्श माना गया है । शब्द- तन्मात्रारूप आकादाने स्पर्श-तममाआावाले वायुकी आबुत किया #ै
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.156)
- **Original**: फिए (स्पर्श-हत्पातारूप] तायुने तिकृत होकर रुप-तम्मात्राकी सृष्टि को। (सूप-तन्णात्रायुक्त) वायुसे तेज उत्पन्न हुआ है, उसका गुण रूप कहा जाता है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.157)
- **Original**: स्पर्या-तन्यान्नारूप बायुने रूप-तन्मात्राबाले तेजकोी आवबृत क्रिया। फिर [रूप-तन्मात्रागय] तेजने भी विकूत होकर रस-तन्पात्राकी रचना की
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.158)
- **Original**: उस (रस- तन्मात्रारूप) से रस-गुणवाला जल हुआ । रस- तत्माषावाके जलको रूप-तन्मात्रामय तेजने आयृत किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.159)
- **Original**: [ररा- उन्मान्रारूप] जलने थिकारकों प्राप्न होकर गन्भ-तन्मात्राकी सृष्टि की, उससे पृथिवों उम्नन्न हुई है जिसका गुण गन्ध माना जाता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.160)
- **Original**: उन-ठउन आकाशादि भूतोंमे तन्मात्रा है [अर्थात्‌ क्रेवल उनके गुण द्राज्दादि ही हैं] इसल्पे वे तन्यात्रा (गुणरूप) हो कहे गये हैं
- **Translation**: 

---

