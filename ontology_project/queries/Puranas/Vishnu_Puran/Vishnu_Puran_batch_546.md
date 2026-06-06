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

### Verse 1 (Vishnu Puran 0.10901)
- **Original**: े8ढ तस्था विवाहे रामाद्या यादवा हरिणा सह । रुक्मिणो नगर जम्मुर्नाप्ना भोजकर्ट द्विज
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10902)
- **Original**: 9 विवाहे तत्र निर्वृत्ति प्राद्युम्नेस्तु महात्मनः । कल्िड्रराजप्रमुखा रुक्मिणं वाक्यमन्लुवन्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10903)
- **Original**: 10 अनक्षज्ञो हली दूते तथास्य व्यसन महत्‌ । न जयामो बल कस्पादयूतेनैन महाबलम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10904)
- **Original**: 19 श्रीपराज्र उवाच तथेति तानाह नृपारूक्मी बलमदान्वितः । सभायां सह रामेण चक्रे द्यूत चर वै तदा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10905)
- **Original**: 12 सहस्नमेक॑ निष्काणां रुक्मिणा विजितो बल: । द्वितीयेषपि पणे चान्यत्सहस्त्रं रुकिमणा जित:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10906)
- **Original**: 13 ततो दशशसहल्लाणि निष्काणां पणमाददे। बलभद्रोउजयत्तानि रुकमी द्यूतविदां वर:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10907)
- **Original**: 14 ततो जहास स्वनवत्कलिज्भाधिपति्विज । दन्तान्विदर्शयन्यूढो रुक्मी चाह मदोद्धत:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10908)
- **Original**: 15 अविद्यो5यं मया द्यूते बलभद्गर:ः पराजित: । मुप्रैवाक्षावलेपाशो योउवमेनेउक्षकोविदान्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10909)
- **Original**: 16 दृष्ठा कलिड्रराजन्त प्रकाशदशनाननम्‌। रुकिमिर्ण चापिदुर्वाक्यं कोप॑ चक्रे हलायुध:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10910)
- **Original**: 17 ततः कोपपरीतात्मा निष्कको्टि समाददे । ग्लहई जग्राह रुकमी चर तदर्थे3क्षानपातयत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10911)
- **Original**: 18 अजयइलदेवस्तं प्राहोश्चैविजितं मया। मयेति रूबमी प्राहोचैरलीकोक्तेरल बल
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10912)
- **Original**: 19 त्वयोक्तो5यं ग्लहस्सत्यं न मयैषोनुमोदितः । एवं त्वया चेद्विजितं विजितं न मया कथ्म्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10913)
- **Original**: 20 श्रीपराज्र उवाच अशथान्तरिक्षे वागुश्लै: प्राह गम्भीरनादिनी । बलदेवस्य त॑ कोप वर्द्धयन्ती महात्मन:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10914)
- **Original**: 29 जित॑ बलेन धर्मेंण रुक्मिणा भाषित॑ मृषा । अनुक्सवापि बच: किज्लित्कृत भवति कर्मणा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10915)
- **Original**: 22 ततो बल: समुत्थाय कोपसंरक्तलोचन: । जघानाष्टापदेनेव रुक्मिणं स महाबल:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10916)
- **Original**: 23 श्रीकिष्णुपुराण
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10917)
- **Original**: अ0 28 हे द्विज ! उसके विवाहमें सम्मिलित होनेके लिये कृष्णचन्द्रके साथ यलभद्र आदि अन्य यादवगण भी रुक्‍्मीकी राजधानी भोजकट नामक नगरकों गये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10918)
- **Original**: जब प्रद्युप्न-पुत्र महात्मा अनिरुद्धक विवाह-सैस्कार हो चुका तो कलिंगरज आदि राजाओंने सकमीसे कहा--
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10919)
- **Original**: “ओ बलभद्र दूतक़ीडा [ अच्छी तरह ] जानते तो हैं नहों तथापि इन्हें उसका व्यसन बहुत है; तो फिर हम इन महाबली रामको जुएसे ही क्यों न जीत लें ?''
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10920)
- **Original**: श्रीपराज्रजी कोल्छे--तब बलके मदसे उन्मत्त स्ुकमोते उन राजाओंसे कहा--'बहुत अच्छा' और सभामें बलरामजोके साथ ग्ूतक्रीडा आरम्य कर दी
- **Translation**: 

---

