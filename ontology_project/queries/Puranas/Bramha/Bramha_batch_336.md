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

### Verse 1 (Bramha 0.6701)
- **Original**: गरुड़का आवाहन किया। वे स्मरण करते ही आ करके कहा था--'देव! युद्धके बिना इन हजार
- **Translation**: 

---

### Verse 2 (Bramha 0.6702)
- **Original**: पहुँचे। भगवान्‌ श्रीकृष्ण बलराम और प्रद्युम्नके भुजाओंसे मुझे बड़ा खेद हो रहा है; क्या कभी ऐसे
- **Translation**: 

---

### Verse 3 (Bramha 0.6703)
- **Original**: साथ गरुड़पर आरूढ़ हो बाणासुरके नगरमें गये। युद्धका अवसर आयेगा, जब कि ये मेरी भुजाएँ
- **Translation**: 

---

### Verse 4 (Bramha 0.6704)
- **Original**: पुरीमें प्रवेश करते समय महाबली प्रमथोंके साथ सफल होंगी?' यदि युद्ध न हो तो इन भुजाओंसे
- **Translation**: 

---

### Verse 5 (Bramha 0.6705)
- **Original**: उनका युद्ध हुआ। श्रीहरि उन सबका संहार क्या लाभ। फिर तो ये मेरे लिये भाररूप ही सिद्ध
- **Translation**: 

---

### Verse 6 (Bramha 0.6706)
- **Original**: करके बाणासुरके भवनके निकट गये। तत्पश्चात्‌ होंगी। यह सुनकर महादेवजीने कहा--'जिस समय
- **Translation**: 

---

### Verse 7 (Bramha 0.6707)
- **Original**: तीन पैर और तीन मस्तकवाले माहेश्वर ज्वरने तुम्हारी मयूर-चिह॒वाली ध्वजा टूट जायगी, उस ' बाणासुरकी रक्षाके लिये शार््र॑धन्वा श्रीकृष्णके समय तुहहें वैसा युद्ध प्रात्त होगा।' इससे बाणासुरको
- **Translation**: 

---

### Verse 8 (Bramha 0.6708)
- **Original**: साथ युद्ध किया। उसके फेंके हुए भस्मके स्पर्शसे बड़ी प्रसन्नता हुई। वह भगबान्‌ शिवको प्रणाम
- **Translation**: 

---

### Verse 9 (Bramha 0.6709)
- **Original**: श्रीकृष्णका शरीर संतप्त हो ठठा और उससे छू करके घर चला आया। कुछ कालके बाद उसकी
- **Translation**: 

---

### Verse 10 (Bramha 0.6710)
- **Original**: जानेपर बलदेवजीने भी शिथिल होकर अपने नेत्र मयूर-ध्वजा टूटकर गिर गयी। यह देखकर उसके
- **Translation**: 

---

### Verse 11 (Bramha 0.6711)
- **Original**: मूँद लिये। इस प्रकार श्रीकृष्णके साथ युद्ध करते हर्षकी सीमा न रही। इसी समय चित्रलेखा अपनी
- **Translation**: 

---

### Verse 12 (Bramha 0.6712)
- **Original**: हुए माहे श्वर ज्वरपर शीघ्र ही वैष्णव ज्वरने आक्रमण योगविद्याके बलसे अनिरुद्धको बाणासुरके भवनमें
- **Translation**: 

---

### Verse 13 (Bramha 0.6713)
- **Original**: किया और उसको भगवान्‌के शरीरसे बाहर निकाल ले आयी। अनिरुद्ध कन्याके अन्तःपुरमें उषाके
- **Translation**: 

---

### Verse 14 (Bramha 0.6714)
- **Original**: दिया। उस समय भगवान्‌ नारायणकी भुजाओंके साथ बिहार करने लगे। यह बात अन्तःपुरके आधातसे महेश्वर ज्वरको बड़ी पीड़ा हुईं। बह रक्षकॉंको मालूम हो गयी। उन्होंने दैत्यराजसे सब
- **Translation**: 

---

### Verse 15 (Bramha 0.6715)
- **Original**: व्याकुल हो उठा। यह देख पितामह ब्रह्माजीने हाल कह सुनाया। बाणासुरने अपने सेवकोंको
- **Translation**: 

---

### Verse 16 (Bramha 0.6716)
- **Original**: आकर कहा--' भगवन्‌! इसे क्षमा कीजिये।' भगवान्‌ अनिरुद्धसे युद्ध करनेकी आज्ञा दी, किंतु शत्रुवीरोंका
- **Translation**: 

---

### Verse 17 (Bramha 0.6717)
- **Original**: बोले--' अच्छा, मैंने क्षमा कर दिया।' यों कहकर दमन करनेवाले अनिरुद्धने लोहेका परिघ लेकर उन
- **Translation**: 

---

### Verse 18 (Bramha 0.6718)
- **Original**: उन्होंने वैष्णव ज्वरको अपनेमें ही लीन कर लिया। सबको मार डाला। सेवकोंके मारे जानेपर बाणासुर
- **Translation**: 

---

### Verse 19 (Bramha 0.6719)
- **Original**: तब माहेश्वर ज्वरने कहा-'भगवन्‌! जो मनुष्य स्वयं ही रथपर आरुढ़ हो अनिरुद्धका बंध करनेके
- **Translation**: 

---

### Verse 20 (Bramha 0.6720)
- **Original**: आपके साथ मेंरे युद्धका स्मरण करेंगे, वे ज्वरहीन लिये उद्यत हुआ। अपनी शक्तिभर युद्ध करनेपर भी
- **Translation**: 

---

