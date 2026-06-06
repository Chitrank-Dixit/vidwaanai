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

### Verse 1 (Markende Puran 0.3061)
- **Original**: तब दूत त्थे गच्छ भगयत्‌ पार्श्व शुध्धनिशुम्भयों:
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3062)
- **Original**: देवीके शरीरक्षे अत्यन्त भयानक और परम उग्र ग्रृहि शुम्ध निशुम्भं॑ च दानवावतिगर्विती। चण्डिका-शक्ति प्रकट हुई, जो सैकड़ों गोदड्ियोंको ये चान्ये दानवास्तम्न युद्धाय समुपस्थिता:
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3063)
- **Original**: माल आवाज करनेत्नली थो
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3064)
- **Original**: उस अपराजिता त्ैलोक्यमिन्रों लभतां देवा: सन्तु श्विर्भुजअ
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3065)
- **Original**: देवोने घूमिल जटावाले महादेवजीसे कहा- भगवन! यूय॑ प्रयात पाताल यदि जीवितुमिच्छथ
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3066)
- **Original**: आप शुप्भ-निशुम्भके पास दूत बनकर जाइये
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3067)
- **Original**: खलावलेपादथ चेद्धयन्तों युद्धकाईसक्षिण:। और उन अत्यन्त गर्बीले दानव शुप्ध एवं तदागच्छत तृप्यन्तु मच्छिवा: पिशितेन वः # 27
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3068)
- **Original**: +शु*1--दोनोंसे कहिये। साध ही उनके अतिरिक्त बतो नियुक्तों दौत्येन तवा देव्या शिव: स्वयम्‌। भी जो दाव बुद्धके लिये वहाँ उपस्थित हों, झ्िवदूतीति लोके5स्मिस्तत: सा स्व्यातिमागता
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3069)
- **Original**: दपएलटए् कफ प्र तेडपि श्रुत्मा सच्रों देव्या: शर्राख्यात महासुरा:। । ! ; 324 अमर्षापूरिता जम्मुर्धत्र' क्रात्याघनी स्थिता
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3070)
- **Original**: ततः प्रथप्रप्ेबाग्रे शरशक्त्यृश्टिवृष्टिफि:। बववर्षुरुद्धतामर्घास्तां देवीममरारय:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3071)
- **Original**: सा च तान्‌ प्रहितान्‌ बाणाउछूलशक्तिपरश्चधान्‌। चिच्छेद लीलयाउ5ध्मातथजुर्मुक्तमड्पुतरिः
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3072)
- **Original**: तस्याग्रत्तस्तथा काली शूलपातचिदारितान्‌। खद्वाड्भपोधितांक्षारीन्‌ कुर्वती व्यच्चरत्तदा
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3073)
- **Original**: कमण्डलुजलाक्षेपडतवीयान्‌ू_ इतौजस:। 2 ग्रह्माणी चाकरोच्छब्रून्‌ येन येन सम धावत्रि 433
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3074)
- **Original**: £दु5 परह्ेश्वरी व्रिशूलेस तथा चकेण वैष्णबी
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3075)
- **Original**: 2828 - दैल्याख्घात कौमारो तधा शक्तणनिकोपना
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3076)
- **Original**: [-+: ऐन्द्रीकुलिशपातेन जझ्तशों दटैत्यटानवा:। । के «2 पेतुर्चिदारिता: पृथ्व्यां रुधिरौधपग्रवर्धिष्य:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3077)
- **Original**: + 3025223424 07 2*/%:8600- तुण्डप्रहारविध्वस्ता .. दंष्टाग्रक्षतवक्षसः
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3078)
- **Original**: उनको भी यह संदेश दीजिये
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3079)
- **Original**: ' दैत्यो! यदि बाराहमूत्यां न्यपत्तश्रक्रेणा क्ष विदारिता:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3080)
- **Original**: तुम जोविते रहना चाहते हो ती पान्तालक्तों लौट नस्जैधिंदारितांभ्रान्यान्‌ भ्क्षमन्ती महासुरान्‌। जाओ । इंजुको जिलोकीका राज्य मिल जाय और नारसिंही अज्ाराजौ मादापूर्णादिगम्बरा
- **Translation**: 

---

