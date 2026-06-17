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

### Verse 1 (Bramha 0.4501)
- **Original**: तब इन्द्रने हँसकर उन्हें सान्त्वना देते हुए वाणोंसे बीँंधता रहा। मेरा यह प्रयत्न उसीका वध
- **Translation**: 

---

### Verse 2 (Bramha 0.4502)
- **Original**: कहा--प्रिये! मैं अपने शरीरकों शपथ खाकर करनेके लिये है। आप मुझे वह शक्ति प्रदान! कहता हूँ--मिन्रवर वृषाकपिके सिया और किसीके कीजिये, जिससे शत्रुका नाश कर सकूँ
- **Translation**: 

---

### Verse 3 (Bramha 0.4503)
- **Original**: घर नहीं जाता। अत: तुम्हें मुझपर संदेह नहीं
- **Translation**: 

---

### Verse 4 (Bramha 0.4504)
- **Original**: 220 + संक्षिप्त ख्रह्मपुराण * करना चाहिये। तुम पतिब्रता और मेरी प्रियतमा
- **Translation**: 

---

### Verse 5 (Bramha 0.4505)
- **Original**: अभीष्ट वस्तु प्राप्त हुई है। मैं समझता हूँ मेरे हो। धर्म करने तथा उचित सलाह देनेमें मेरी
- **Translation**: 

---

### Verse 6 (Bramha 0.4506)
- **Original**: मित्रके बलसे अब यह इन्द्रपद स्थिर रहेगा। सदा सहायता करती हो। साथ ही संतानवती
- **Translation**: 

---

### Verse 7 (Bramha 0.4507)
- **Original**: तीर्थोमें गौतमी गड्डा और देवताओंमें भगवान्‌ और कुलीन भी हो। फिर तुम्हारे सिवा दूसरी विष्णु और शिव श्रेष्ठ हैं। इन्होंकी कृपासे मुझे कौन स्त्री मेरी प्रियतमा हो सकती है। तुम्हारे
- **Translation**: 

---

### Verse 8 (Bramha 0.4508)
- **Original**: सब मनोवाज्छित वस्तुएँ प्राप्त हुई हैं। यह ही उपदेशसे मैं महानदी गौतमी गड्भ्राके तटपर
- **Translation**: 

---

### Verse 9 (Bramha 0.4509)
- **Original**: त्रिलोकविख्यात तीर्थ मेरी प्रसन्नताको बढ़ानेवाला गया और वहाँ भगवान्‌ विष्णु, शिव तथा मित्र
- **Translation**: 

---

### Verse 10 (Bramha 0.4510)
- **Original**: है। अत: मैं क्रमशः सम्पूर्ण देवताओंसे यह वृषाकपिके प्रसादसे दुःखसागरके पार हुआ
- **Translation**: 

---

### Verse 11 (Bramha 0.4511)
- **Original**: प्रार्थना करता हूँ; महर्षिगण, गद्गा, विष्णु तथा और अब यहाँ राज्यसे च्युत न होनेवाला इन्द्र
- **Translation**: 

---

### Verse 12 (Bramha 0.4512)
- **Original**: शिव भी मेरी प्रार्थनाका अनुमोदन करें। देवताओं! हूँ। यह सब तुम्हारे सहयोगका फल है। जहाँ
- **Translation**: 

---

### Verse 13 (Bramha 0.4513)
- **Original**: गड्गजाके दोनों तटोंपर एक ओर इन्द्रेश्वरतीर्थ है और स्वामीके चित्तका अनुसरण करनेवाली पतिक्रता
- **Translation**: 

---

### Verse 14 (Bramha 0.4514)
- **Original**: दूसरी ओर अग्जकतीर्थ। इन्द्रेश्वरमें भगवान्‌ शिव स्त्री हो, वहाँ कौन-सा कार्य असाध्य है। वहाँ रहते हैं और अब्जकमें साक्षात्‌ भगवान्‌ विष्णु। वे तो मोक्ष भी दुर्लभ नहीं है। फिर अर्थ, काम
- **Translation**: 

---

### Verse 15 (Bramha 0.4515)
- **Original**: अपनी उपस्थितिसे दण्डकबनको पतित्र करते हैं। आदिकी तो बात हो कया है। पत्नी भी परम मित्र
- **Translation**: 

---

### Verse 16 (Bramha 0.4516)
- **Original**: इनके बीचमें जो-जो तीर्थ हैं, वे सब पुण्यदायक है। बह लोक और परलोक दोनोंमें हितकारिणी
- **Translation**: 

---

### Verse 17 (Bramha 0.4517)
- **Original**: हैं। उनमें स्नान करनेमात्रसे सबकी मुक्ति होती है। होती है। पत्नी भी यदि कुलीन, प्रिय बोलनेवाली, ' पापी पापसे मुक्त होते हैं और धर्मात्मा पुरुष पतिव्रता, रूपवती, गुणबती तथा सम्पत्ति और
- **Translation**: 

---

### Verse 18 (Bramha 0.4518)
- **Original**: अपनी पाँच-पाँच पीढ़ीके पितरोंसहित परममोक्षके विपत्तिमें समान रूपसे साथ देनेवाली हो तो
- **Translation**: 

---

### Verse 19 (Bramha 0.4519)
- **Original**: भागी होते हैं। यहाँ आकर जो लोग याचकोंको उसके द्वारा इस त्रिलोकीमें कुछ भी असाध्य
- **Translation**: 

---

### Verse 20 (Bramha 0.4520)
- **Original**: तिलभर भी दान करते हैं, वह दान दाताओंके नहीं: है। प्रिये! तुम्हारी बुद्धिसे हो मुझे यह
- **Translation**: 

---

