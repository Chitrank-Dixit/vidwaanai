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

### Verse 1 (Bramha 0.3181)
- **Original**: कहा-“महाभाग ! मुझे आगमें डाल दीजिये। मैं योग्य ही उत्तम बात कही है; किंतु इस विषयमें
- **Translation**: 

---

### Verse 2 (Bramha 0.3182)
- **Original**: अपने शरीरसे इस दुःखी व्याधको तृप्त करूँगी। मुझे कुछ और भी कहना है, उसे सुनो। कोई एक ' सुब्रत! ऐसा करनेसे तुम अतिथि-सत्कार करनेवाले हजार प्राणियोंका भरण-पोषण करता है। दूसरा
- **Translation**: 

---

### Verse 3 (Bramha 0.3183)
- **Original**: पुण्यात्माओंके लोकमें जाओगे। दसका ही निर्वाह करता है और कोई ऐसा है, जो
- **Translation**: 

---

### Verse 4 (Bramha 0.3184)
- **Original**: कपोत बोला--शुभे ! मेंर जीते-जी यह तुम्हारा सुखपूर्वक केवल अपनी जीविकाका काम चला
- **Translation**: 

---

### Verse 5 (Bramha 0.3185)
- **Original**: धर्म नहीं है। मुझे ही आज्ञा दो। मैं ही आज लेता है; किंतु हमलोग ऐसे जीवॉमेंसे हैं, जो अपना
- **Translation**: 

---

### Verse 6 (Bramha 0.3186)
- **Original**: अतिधि-यज्ञ करूँगा। ही पेट बड़े कष्टसे भर पाते हैं। कुछ लोग खाई
- **Translation**: 

---

### Verse 7 (Bramha 0.3187)
- **Original**: यों कहकर कपोतने सबको शरण देनेवाले खोदकर उसमें अन्न भरकर रखते हैं। कुछ लोग
- **Translation**: 

---

### Verse 8 (Bramha 0.3188)
- **Original**: भक्तवत्सल विश्वरूप चतुर्भुज महाविष्णुका स्मरण कोठेभर धानके धनी होते हैं और कितने ही घड़ोंमें
- **Translation**: 

---

### Verse 9 (Bramha 0.3189)
- **Original**: करते हुए अग्निकी तीन बार परिक्रमा कौ; फिर धान भरकर रखते हैं; परंतु हमारे पास तो ठतना ही
- **Translation**: 

---

### Verse 10 (Bramha 0.3190)
- **Original**: व्याधसे यह कहते हुए अग्निमें प्रवेश किया कि संग्रह होता है, जितना अपनी चोंचमें आ जाय।
- **Translation**: 

---

### Verse 11 (Bramha 0.3191)
- **Original**: 'मुझे सुखपूर्वक उपयोगमें लाओ।' कपोतने शुभे! तुम्हीं बताओ, ऐसी दशामें इस थके-माँदे
- **Translation**: 

---

### Verse 12 (Bramha 0.3192)
- **Original**: अपने जीवनको अग्निमें होम दिया, यह देख अतिथिका आदर-सत्कार मैं किस प्रकार करूँ?
- **Translation**: 

---

### Verse 13 (Bramha 0.3193)
- **Original**: व्याध कहने लगा-'अहो! मेरे इस मनुष्य- कपोतीने कहा--नाथ! अग्नि, जल, मीठी
- **Translation**: 

---

### Verse 14 (Bramha 0.3194)
- **Original**: शरीरका जीवन धिक्कार देने योग्य है, क्योंकि वाणी, तृण और काष्ठ आदि जो भी सम्भव हो,
- **Translation**: 

---

### Verse 15 (Bramha 0.3195)
- **Original**: मेरे ही लिये पक्षिराजने यह साहसपूर्ण कार्य वह अतिथिको देना चाहिये। यह व्याध सर्दीसे
- **Translation**: 

---

### Verse 16 (Bramha 0.3196)
- **Original**: किया है।' यों कहते हुए व्याधसे कपोतीने कष्ट पा रहा है।* कहा--'महाभाग! अब मुझे छोड़ दो। देखो, अपनी प्यारी स्त्रीका कथन सुनकर पक्षिराज
- **Translation**: 

---

### Verse 17 (Bramha 0.3197)
- **Original**: मेरे ये पतिदेव मुझसे दूर चले जा रहे हैं।' कपोतने पेड्पर चढ़कर सब ओर देखा तो कुछ
- **Translation**: 

---

### Verse 18 (Bramha 0.3198)
- **Original**: उसकी बात सुनकर व्याध सहम गया और तुरंत दूरीपर उसे आग दिखायी दी। वहाँ जाकर वह
- **Translation**: 

---

### Verse 19 (Bramha 0.3199)
- **Original**: ही पिंजड़ेमें पड़ी हुई कपोतीकों उसने छोड़ चोंचसे एक जलती हुई लकड़ी उठा लाया और
- **Translation**: 

---

### Verse 20 (Bramha 0.3200)
- **Original**: दिया। तब उसने भी पति और अग्निकी परिक्रमा व्याधके आगे रखकर अग्निको प्रज्वलित किया;
- **Translation**: 

---

