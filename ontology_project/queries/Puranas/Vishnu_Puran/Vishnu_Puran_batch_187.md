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

### Verse 1 (Vishnu Puran 0.3721)
- **Original**: 48 सब्याकाले च सम्म्राप्ते रौद्े परमदारुणे । मन्देहा राक्षसा घोराः सूर्यमिच्छन्ति खादितुम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3722)
- **Original**: 49 पअ्रजापतिकृतः शापस्तेयां मैत्रेय रक्षसाम्‌। अक्षयत्य॑ शरीराणां मरणं चर दिने दिने
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3723)
- **Original**: 50 ततः सूर्यस्य तैर्युद्ध॑ं भवत्यत्यन्तदारुणम्‌ । ततो ब्विजोत्तमास्तोयं सद्लिपन्ति महामुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3724)
- **Original**: 51 उधकारब्रह्मसंयुक्ते गायत्या चाभिपन्त्रितम्‌। तेन दह्हान्ति ते पापा व्रजीभूतेन वारिणा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3725)
- **Original**: 52 अमिह्लेत्रे हूृयते या समन्‍्त्रा प्रथमाहृतिः । सूर्यो ज्योतिः सहस्नांशुस्तया दीप्यति भास्कर:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3726)
- **Original**: 53 ओछ्डारो भगवान्विष्णुस्रिधापा वचसां पति: । तदुश्चारणतस्ते तु विनाझ यान्ति राक्षसा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3727)
- **Original**: 54 वैष्णवोंडशञ: पर: सूर्यो यो5न्तज्योतिरसम्प्रवम्‌ । अभिधायक 33“कारस्तस्य तत्रेरकः पर:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3728)
- **Original**: 55 ज्योतिश्चक्रके मध्यमें स्थित घुव अति मनन्‍्द गतिसे घूमता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3729)
- **Original**: हे मैक्ेय ! जिस प्रकार कुल्त्रक-चक्रकी नाभि अपने स्थानपर ही घूमती रहती है, उसी प्रकार धुत भी अपने स्थानपर ही घूमता रहता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3730)
- **Original**: इस प्रकार उत्तर तथा दक्षिण सीमाओंके मध्यमें मण्डल्मकार घूमते रहनेसे सूर्यकों गति दिन अथवा राजिके समय मन्द अथका शीघ्र हो जाती है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3731)
- **Original**: जिस अयममें सूर्यकी गत्ति दितके समय मन्द होती है उसमें रातिके समय शीघ्र होती है तथा जिस समय राध्रि-कारुसें शीघ्र होतो है डस समय दिनमें मनन्‍्द हो जाती है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3732)
- **Original**: हे द्विज ! सूर्यकों सदा एक बराबर मार्ग ही पार करना पड़ता है; एक दिन-रात्रिमें यह समस्त राहियोंका भोग कर लेता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3733)
- **Original**: सूर्य छः रशियोंको रात़िके समय भोगता है और छःकों दिनके समय
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3734)
- **Original**: राशियोंके परिमाणानुसार ही दिनका बवुना- घटना होता है तथा रात्रिकी छघुता-दीर्घता भी राहियोकिे परिमाणसे ही होती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3735)
- **Original**: राशियोंके भोगानुसार ही दिन अथवा रात्रिकों लघुता अथवा दीर्घता होती है। उत्तरायणमें सूर्यकी गति राज्रिकालमें ज्लीघ होती है तथा दिनमें मन्द
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3736)
- **Original**: दक्षिणायनमें उसकी गति इसके विपरीत होती है । 46-47
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3737)
- **Original**: रात्रि उपा कहलाती है तथा दिन व्युष्टि (प्रभात) कहा जाता है; इन उषा तथा व्युष्टिके बीचके समयको सन्ध्या कहते हैं *
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3738)
- **Original**: इस अति दारूण और भयानक सश्या- कालके उपस्थित होनेपर मन्देहा नामक भयंकर राक्षसगण सूर्यकों खाना याहते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3739)
- **Original**: हे मैप्रेय ! उन राक्षसॉंको प्रजापतिका यह शाप है कि उनका शरीर अक्षय रहकर भी मरण नित्यप्रति हो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3740)
- **Original**: अतः सम्ध्या-काल्में उनका सूर्यसे अति भीषण युद्ध होता है; हे महामुने ! उस समय द्विजोतमगण जो बद्मस्वरूप 3>कार तथा गायत्रौसे अभिमन्त्रित जल छोड़ते हैं उस वज़स्वरूप जलसे वे दुष्ट राक्षस दग्ध हो जाते हैं
- **Translation**: 

---

