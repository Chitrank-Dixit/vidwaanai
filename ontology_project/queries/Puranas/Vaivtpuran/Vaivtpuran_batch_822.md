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

### Verse 1 (Vaivtpuran 543.14754)
- **Original**: आपको नमस्कार है। असंख्य ब्रह्माण्डोंमें आप देखा। वे मुस्करा रहे थे। तत्पश्चात्‌ उन्होंने चतुर्भुज
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14755)
- **Original**: ही ब्रह्मा, विष्णु और शिव-रूपमें निवास करते विष्णुके रूपमें उनको सामने खड़े देखा। लक्ष्मी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14756)
- **Original**: हैं। आप ही सबके आदिकारण हैं। विश्वेश्वर और और सरस्वती-ये दो देवियाँ उनके अगल- [विश्व दोनों आपके ही स्वरूप हैं; आपको बगलमें खड़ी थीं। वे वनमालासे विभूषित थे।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14757)
- **Original**: नमस्कार है। गोपाज्जनाओंके प्राणवल्लभ! आपको सुतन्द, नन्द और कुमुद आदि पार्षद उनकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14758)
- **Original**: नमस्कार है। गणेश और ईश्वर आपके ही रूप सेवामें उपस्थित थे। सिद्धोंक समुदाय भक्तिभावसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14759)
- **Original**: हैं। आपको नमस्कार है। आप देवगणोंके स्वामी नम्न हो उन परात्पर प्रभुकी सेवा कर रहे थे।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14760)
- **Original**: तथा श्रीराधाके प्राणवल्लभ हैं; आपको बारंबार फिर, दूसरे ही क्षण अक्रूरने श्रीकृष्णको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14761)
- **Original**: नमस्कार है। आप ही राधारमण तथा राधाका महादेवजीके रूपमें देखा। उनके पाँच मुख और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14762)
- **Original**: रूप धारण करते हैं। राधाके आराध्य देवता तथा प्रत्येक मुखमें तीन-तीन नेत्र थे। अद्गकान्ति शुद्ध
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14763)
- **Original**: राधिकाके प्राणाधिक प्रियतम भी आप ही हैं; स्फटिक-मणिके समान उज्वल थी। नागराजके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14764)
- **Original**: आपको नमस्कार है। राधाके वशमें रहनेवाले, आभूषण उनकी शोभा बढ़ाते थे। दिशाएँ ही
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14765)
- **Original**: राधाके अधिदेवता और राधाके प्रियतम ! आपको उनके लिये बस्त्रका काम देती थीं। योगियोंमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14766)
- **Original**: नमस्कार है। आप राधाके प्राणोंक अधिष्ठाता श्रेष्ठ बे परब्रह्म शिव अपने अज्ञोंमें भस्म रमाये,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14767)
- **Original**: देवता हैं तथा सम्पूर्ण विश्व आपका ही रूप है; सिरपर जटा धारण किये और हाथमें जप-माला
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14768)
- **Original**: आपको नमस्कार है। बेदोंने जिनकी स्तुति की लिये ध्यानमें स्थित थे। है, वे परमात्मा तथा बेदज्ञ विद्वान भी आप ही तदनन्तर एक ही क्षणमें श्रीकृष्ण उन्हें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14769)
- **Original**: हैं। वेदोंके ज्ञानसे सम्पन्न होनेके कारण आप
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14770)
- **Original**: 642 » संक्षिप्त ग्रह्मवैवर्तपुराण * #% 6 # 6 ## ##ऋकऋऋऋशऋऋऋ क्र 8
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14771)
- **Original**: #क्कककऋकऋककऋकऋकऋ कक ऋ 44 4 कफ ऋऋऋऋ 9 4 %6 54849 5555 वेदी कहे गये हैं; आपको नमस्कार है। वेदोंके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14772)
- **Original**: प्रिय भार्याकी उपलब्धि होती है। निर्धनकों धन, अधिष्ठाता देवता और बीज भी आप ही हैं;
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14773)
- **Original**: भूमिहीनको उर्वरा भूमि, संतानहीनको संतान और आपको नमस्कार है। जिनके रोमकूपोंमें असंख्य
- **Translation**: 

---

