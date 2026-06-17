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

### Verse 1 (Vaivtpuran 48.4674)
- **Original**: गोलोकसे इस भूतलपर आना पड़ा था। उस समय महालक्ष्मीका प्राकट्य हुआ है। वे ही शस्यकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 48.4675)
- **Original**: वे वृषभानु गोपके घरमें अवतीर्ण हुई थीं। बहाँ अधिष्ठात्री देवी तथा गृहलक्ष्मीके रूपमें भी आविर्भूत
- **Translation**: 

---

### Verse 3 (Vaivtpuran 48.4676)
- **Original**: उनकी माता कलावती थीं। (अध्याय 48) #न्‍ल>ल्‍ >#सिय00720200 0 * राधा भजति श्रीकृष्ण स च तां च परस्परम्‌ । उभयोः सर्वसाम्य॑ च सदा सन्‍्तो वदन्ति च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 48.4677)
- **Original**: (प्रकृतिखण्ड 48। 38) । ग्राणाधिष्ठातृदेवी. च.. तस्वैव परमात्मन:। (प्रकृतिखण्ड ड8। 47) + आन्रह्मस्तम्बपर्यनत॑ सर्व॑ मिथ्यैव पार्वति । भज सत्य पर॑ ब्रह्म राधेशं त्रिगुणात्परम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 48.4678)
- **Original**: (प्रकृतिखण्ड 48
- **Translation**: 

---

### Verse 6 (Vaivtpuran 48.4679)
- **Original**: + प्रकृतिखण्ड + 251 44000 04 02)
- **Translation**: 

---

### Verse 7 (Vaivtpuran 48.4680)
- **Original**: 0] 0 000 00] 0 ] 0 । 0
- **Translation**: 

---

### Verse 8 (Vaivtpuran 48.4681)
- **Original**: ।]]घ88ऋ] श्रीराधा और श्रीकृष्णके चरित्र तथा श्रीराधाकी पूजा-परम्पराका अत्यन्त संक्षिप्त परिचय श्रीमहादेवजी कहते हैं--पार्वति! एक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 48.4682)
- **Original**: बहाने शैशवावस्थामें ही गोकुल पहुँचा दिये गये समयकी बात है, श्रीकृष्ण विरजा नामवाली
- **Translation**: 

---

### Verse 10 (Vaivtpuran 48.4683)
- **Original**: थे। वहाँ श्रीकृष्णकी माता जो यशोदा थीं, उनका सखीके यहाँ उसके पास थे। इससे श्रीराधाजीको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 48.4684)
- **Original**: सहोदर भाई 'रायाण' था। गोलोकमें तो वह क्षोभ हुआ। इस कारण विरजा वहाँ नदीरूप
- **Translation**: 

---

### Verse 12 (Vaivtpuran 48.4685)
- **Original**: श्रीकृष्णका अंशभूत गोप था, पर इस अबतारके होकर प्रवाहित हो गयी। विरजाकी सस्त्रियाँ भी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 48.4686)
- **Original**: समय भूतलपर वह श्रीकृष्णका मामा लगता था। छोटी-छोटी नदियाँ बनीं। पृथ्वीकी बहुत-सी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 48.4687)
- **Original**: जगत्स्रष्टा बिधाताने पुण्यमय वृन्दावनमें श्रीकृष्णके नदियाँ और सातों समुद्र विरजासे ही उत्पन्न हैं। साथ साक्षात्‌ श्रीराधाका विधिपूर्वक विवाहकर्म राधाने प्रणयकोपसे श्रीकृष्णके पास जाकर उनसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 48.4688)
- **Original**: सम्पन्न कराया था। गोपगण स्वप्रमें भी श्रीराधाके कुछ कठोर शब्द कहे। सुदामाने इसका विरोध
- **Translation**: 

---

### Verse 16 (Vaivtpuran 48.4689)
- **Original**: चरणारविन्दका दर्शन नहीं कर पाते थे। साक्षात्‌ किया। इसपर लीलामयी * श्रीराधाने उसे असुर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 48.4690)
- **Original**: राधा श्रीकृष्णके वक्ष:स्थलमें वास करती थीं और होनेका शाप दे दिया। सुदामाने भी लीलाक्रमसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 48.4691)
- **Original**: छायाराधा रायाणके घरमें। ब्रह्माजीने पूर्वकालमें ही श्रीराधाकों मानवीरूपमें प्रकट होनेकी बात
- **Translation**: 

---

### Verse 19 (Vaivtpuran 48.4692)
- **Original**: श्रीराधाके चरणारविन्दका दर्शन पानेके, लिये कह दी। सुदामा माता राधा तथा पिता श्रीहरिको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 48.4693)
- **Original**: पुष्करमें साठ हजार वर्षोतक तपस्या की थी; उसी प्रणाम करके जब जानेको उद्यत हुआ तब श्रीराधा
- **Translation**: 

---

