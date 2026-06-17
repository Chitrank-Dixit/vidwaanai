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

### Verse 1 (Vaivtpuran 48.4694)
- **Original**: तपस्याके फलस्वरूप इस समय उन्हें श्रीराधा- पुत्रविरहसे कातर हो आँसू बहाने लगीं। श्रीकृष्णने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 48.4695)
- **Original**: चरणोंका दर्शन प्राप्त हुआ था। गोकुलनाथ श्रीकृष्ण उन्हें समझा-बुझाकर शान्त किया और शीघ्र
- **Translation**: 

---

### Verse 3 (Vaivtpuran 48.4696)
- **Original**: कुछ कालतक वृन्दावनमें श्रीराधाके साथ आमोद- उसके लौट आनेका विश्वास दिलाया। सुदामा ही
- **Translation**: 

---

### Verse 4 (Vaivtpuran 48.4697)
- **Original**: प्रमोद करते रहे। तदनन्तर सुदामाके शापसे उनका तुलसीका स्वामी शट्डुचूड़ नामक असुर हुआ था,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 48.4698)
- **Original**: श्रीराधाके साथ वियोग हो गया। इसी बौचमें जो मेरे शूलसे विदीर्ण एवं शापमुक्त हो पुनः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 48.4699)
- **Original**: श्रीकृष्णने पृथ्वोका भार उतारा। सौ वर्ष पूर्ण हो गोलोक चला गया। सती राधा इसी वाराहकल्पमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 48.4700)
- **Original**: जानेपर तीर्थयात्राके प्रसड़से श्रीराधाने श्रीकृष्णका गोकुलमें अवतीर्ण हुई थीं। वे ब्रजमें वृषभानु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 48.4701)
- **Original**: और श्रीकृष्णने श्रीराधाका दर्शन प्राप्त किया। वैश्यकी कन्या हुईं। वे देवी अयोनिजा थों,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 48.4702)
- **Original**: तदनन्तर तत्त्वज्ञ श्रीकृष्ण श्रीराधाके साथ गोलोकधाम माताके पेटसे नहीं पैदा हुई थीं। उनकी माता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 48.4703)
- **Original**: पधारे। कलावती (कौर्तिदा) और यशोदा भी कलावतीने अपने गर्भमें “वायु” को धारण कर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 48.4704)
- **Original**: श्रीराधाके साथ ही गोलोक चली गयीं। रखा था। उसने योगमायाकी प्रेरणासे वायुकों ही। प्रजापति द्रोण नन्‍्द हुए। उनकी पत्नी धरा जन्म दिया; परंतु वहाँ स्वेच्छासे श्रीराधा प्रकट हो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 48.4705)
- **Original**: यशोदा हुईं। उन दोनोंने पहले की हुई तपस्याके गयीं। बारह वर्ष बीतनेपर उन्हें नूतन यौवनमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 48.4706)
- **Original**: प्रभावसे परमात्मा भगवान्‌ श्रीकृष्णको पुत्ररूपमें प्रवेश करती देख माता-पिताने “रायाण' वैश्यके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 48.4707)
- **Original**: प्राप्त किया था। महर्षि कश्यप वसुदेव हुए थे। साथ उसका सम्बन्ध निश्चित कर दिया। उस
- **Translation**: 

---

### Verse 15 (Vaivtpuran 48.4708)
- **Original**: उनकी पत्नी सती साध्वी अदिति अंशत: देवकीके समय श्रीराधा घरमें अपनी छायाको स्थापित
- **Translation**: 

---

### Verse 16 (Vaivtpuran 48.4709)
- **Original**: रूपमें अवतीर्ण हुई थीं। प्रत्येक कल्पमें जब करके स्वयं अन्तर्धान हो गयीं। उस छायाके साथ
- **Translation**: 

---

### Verse 17 (Vaivtpuran 48.4710)
- **Original**: भगवान्‌ अवतार लेते हैं, देवमाता अदिति तथा हो उक्त रायाणका विवाह हुआ। देवपिता कश्यप उनके माता-पिताका स्थान ग्रहण “जगत्पति श्रीकृष्ण कंसके भवसे रक्षाके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 48.4711)
- **Original**: करते हैं। श्रीराधाकी माता कलावती (कीर्तिंदा)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 49.4712)
- **Original**: पितरोंकी मानसी कन्या थी। गोलोकसे वसुदाम
- **Translation**: 

---

### Verse 20 (Vaivtpuran 49.4713)
- **Original**: राधा श्रीकृष्णकी पूजनीया हैं और भगवान्‌ श्रीकृष्ण गोप ही वृषभानु होकर इस भूतलपर आये थे।
- **Translation**: 

---

