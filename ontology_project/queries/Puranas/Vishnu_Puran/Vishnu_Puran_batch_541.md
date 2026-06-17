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

### Verse 1 (Vishnu Puran 0.10801)
- **Original**: श्रीकृष्णचन्द्रके प्रार्थना करनेपर भी उनसे द्वेष करनेके शिशुपालाय जरासन्थप्रचोदित: कारण सुक्‍्मीने उन्हें रुक्मिणी न दी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10802)
- **Original**: महापयक्रमी 2 च रुविमिणा सादे £ भीष्मकने जरासन्धकी प्रेरणासे रुक्मीसे सहमत होकर रुविमणीमुरुविक्रमः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10803)
- **Original**: 3 शिक्षुपालको रुजिमिणी देनेका निश्चय किया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10804)
- **Original**: तब विवाहार्थ ततः सर्वे जरासन्धमुखा नृपाः । शिद्वुपालके हिलैषों जरासन्ध आदि सघ्पूर्ण राजागण भीष्मकस्य पुर॑ जम्मुह्झिशुपालप्रियेधिण: । 4
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10805)
- **Original**: विवाहमें सम्मिलित होनेके लिये मम नगरमें ये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10806)
- **Original**: इधर बलभद्र आदि यदूवंशियोंके सहित कृष्णोअपि बलभब्राहौय॑दुभि: परिवारितः। .
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10807)
- **Original**: कष्णचन््र थी चेटियजका सिवाहोत्सव देखनेके लिये प्रययौ कुण्डिन द्रढ्ुं विवाह चेहाभूभृतः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10808)
- **Original**: 5 कुष्डिनपुर आये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10809)
- **Original**: श्लोभामिनि विवाहे तु ता कन्या हतवान्हरि: । तदनन्तर बिवाहका एक दिन रहनेपर अपने विपक्षियॉका भार बल्भद्र आदि ब्रद्धुऑको सौंपकर श्रीहरिने उस कन्याका हरण कर लिया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10810)
- **Original**: तब औमान्‌ ततश्ष पौण्डुकइश्रीमान्दन्तवक्रो विदूरथ: । पौण्डक, दन्तबक्र, विदूरथ, शिश्ुपाल, जरासन्ध और झिशुपालजरासन्थशाल्वाद्याश्न॒ महीभृतः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10811)
- **Original**: झाल्य आदि राजाओनि क्रोधित होकर श्रीहरिको मारनेका चक्कुरुद्योगमुत्तमम्‌ महान्‌ उद्योग किया, फिन्तु ये सब बलराम आदि 4 र्जि 44 हि. है नि यदुश्नेष्ठोंसे मुठभेड़ होनेपर पराजित हो गये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10812)
- **Original**: तब रामाहोर्यदुपुड्वैः रुक्‍्मीने यह प्रतिज्ञाकर कि 'मैं युद्धमें कृष्णकों मारे बिना कुण्डिन न प्रवेक्ष्यामि ह्ाहत्वा युधि केशवम्‌ । कुण्डिनपुरमें प्रवेश न करूँगा' कृष्णको मारनेके लिये कृत्वा प्रतिज्ञां रुक्मी च हन्तुं कृष्णमनुद्गुत:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10813)
- **Original**: उनका पीछा किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10814)
- **Original**: किन्तु श्रीकृष्णने छीस्प्से हो मृतल अतिको ह्न है हाथी, चोड़े, रथ और पदातियोंसे युक्त उसकी सेनाको नष्ट हत्वा बल सनागा्व॑ ! करके उसे जीत लिया और पृथित्रीमें गिरा दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10815)
- **Original**: निर्जित्य रुक्मिणं सम्यगुपयेमे च रुक्मिणीम्‌।
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10816)
- **Original**: राक्षस-विवाहसे मिली हुई रुक्मिणीका सम्यक्‌ (वेदोक्त) राक्षसेन मधुसूदनः रीतिसे पाणिग्रहण किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10817)
- **Original**: उससे उनके कामदेबके है विवाहेन सम्प्राप्तां मधुसूदन:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10818)
- **Original**: 11 अंदासे उत्पन्न हुए वीर्यवान्‌ प्रद्युन्नजीका जञ हुआ, जिन्हें तस्यां जज्ञे च प्द्मुस्े मदनांशस्सवीर्यवान्‌ । शम्बरासुर हर ले गया था और फिर जिन्होंने [ काल- जहार शाम्बरो य॑ वै यो जघान चर हम्बरम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10819)
- **Original**: क्रमसे ] शम्बरासुरका वध किया था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10820)
- **Original**: विपक्षभारमासज्य रामादिष्वुथ॒ बन्धुषु
- **Translation**: 

---

