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

### Verse 1 (Vaivtpuran 543.14894)
- **Original**: हाथोंमें रस्सी लिये नंग-धड़ंग दिखायी देते थे। वहाँके पार्षदोंमें एक पार्षद हो गया। वहाँ अपने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14895)
- **Original**: एक विधवा शूद्री दृष्टिगोचर हुई, जो नंगी थी और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14896)
- **Original**: + श्रीकृष्णजन्मखण्ड * 647 #%$%$%##%#%&# ## # &# ###ऋ#& &%& ##ऋ#ऋ#ऋ###ऋऋऊऋऊऋऋ%ऊ$ऊ%ऊ%#%%5%$#$% 44 ##### ############%ऋ#%ऋ% कक जिसकी नाक कटी हुई थी। वह हँसती थी। उसने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14897)
- **Original**: पुरुषों तथा युद्धकुशल पुरुषोंको यथास्थान बैठाया। चूनेका तिलक लगा रखा था और उसके सफेद नारद! इसी समय बलरामके साथ भगवान्‌ और काले केश ऊपरकी ओर उठे थे। वह एक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14898)
- **Original**: श्रीकृष्ण रड्रभूमिमें आये और महादेवजीके हाथमें तलवार और दूसरेमें खप्पर लिये हुए थी।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14899)
- **Original**: धनुषको लीलापूर्वक बीचसे ही तोड़ डाला। धनुष उसकी जीभ लपलपा रही थी और उसके गलेमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14900)
- **Original**: टूटनेकी भयंकर आवाजसे सारी मथुरापुरी बहरी- मुण्डमाला पड़ी थी। उसके सिवा कंसने गदहा,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14901)
- **Original**: सी हो गयी। कंसको बड़ा दुःख हुआ और भैंस, बैल, सृअर, भालू, कौआ, गीध, कड्डढू,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14902)
- **Original**: देवकौनन्दन श्रीकृष्ण हर्षसे खिल उठे। द्वास्वर्ती बानर, सफेद कुत्ता, घड़ियाल, सियार, भस्मपुञ्ल,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14903)
- **Original**: मल्लसहित हाथीका वध करके वे सभामें उपस्थित हड्डियोंका ढेर, ताड़का फल, केश, कपास, बुझे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14904)
- **Original**: हुए। योगीजनोंने उन्हें साक्षात्‌ परमात्मदेव परमेश्वरके अद्भार (कोयले), उल्का, चितापर चढ़ा हुआ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14905)
- **Original**: रूपमें देखा। वे अपने हृदयकमलमें जिस मुर्दा, कुम्हार और तेलीके चक्र, टेढ़ी-मेढ़ी [स्वरूपका ध्यान करते थे, वही उन्हें बाहर कौड़ी, मरघट, अधजला काठ, सूखा काठ, कुश,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14906)
- **Original**: दृष्टिगोचर हुआ। राजाओंकी दृष्टिमें वे सर्वशासक तृण, चलता हुआ धड़, मुर्देका चिह्लाता हुआ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14907)
- **Original**: दण्डधारी राजेन्द्र थे। माता-पिताने उनको मस्तक, आगसे जला हुआ स्थान, भस्म-युक्त [स्तनपान करनेवाले दुधमुँहे बालकके रूपमें सूखा तालाब, जली मछली, लोहा, दावानलसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14908)
- **Original**: देखा। कामिनियोंकी दृष्टिमें वे करोड़ों कन्दर्पोंकी जलकर बुझे हुए बन, गलित कोढ़से युक्त नंगा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14909)
- **Original**: लावण्य-लीला धारण करनेवाले रसिकशेखर थे। शूद्र, शिखा खोले और अत्यन्त रोषसे भरकर शाप
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14910)
- **Original**: कंसने कालपुरुष समझा और उसके भाइयोंने देते हुए ब्राह्मण एवं गुरु, अधिक कुपित हुए
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14911)
- **Original**: शत्रु। मह्लेंने अपनी मृत्युका स्थान माना और संन्‍्यासी, योगी एवं वैष्णव मनुष्य देखे। ऐसा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14912)
- **Original**: यादवोंने उनको प्राणोंक समान प्रिय देखा। दुःस्वप्न देख कंसकी नींद खुल गयी और उसने श्रीकृष्णने सभामें बैठे हुए मुनियों, ब्राह्मणों माता, पिता, भाई तथा पत्नीसे वह सब कह
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14913)
- **Original**: तथा माता, पिता एवं गुरुजनोंको नमस्कार किया। सुनाया। पत्नी प्रेमसे विहल होकर रोने लगी।
- **Translation**: 

---

