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

### Verse 1 (Vaivtpuran 17.1054)
- **Original**: परमात्मा मुखसे मन्द-मन्द मुस्कानकी आभा धर्म तथा दिशाओंके स्वामी दिक्पाल भी एक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.1055)
- **Original**: बिखेरते रहते हैं। वैष्णव संत उन्हीं सत्यस्वरूप देशके निवासी हैं। ब्रह्मा, विष्णु और शिव आदि
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.1056)
- **Original**: श्यामसुन्दका सदा भजन और ध्यान करते हैं। देवेश्वर, देवसमूह और चराचर प्राणी--ये सब
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.1057)
- **Original**: आप लोग भी वैष्णव ही हैं और मुझसे पूछ रहे भिन्न-भिन्न ब्रह्माण्डोंमें अनेक हैं। उन ब्रह्माण्डों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.1058)
- **Original**: हैं कि 'तुम्हारा जन्म किसके बंशमें हुआ है? तथा और देवताओंकी गणना करनेमें कौन समर्थ है?
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.1059)
- **Original**: तुम किस मुनीन्द्रके शिष्य हो?' ऐसा प्रश्न मुझसे उन सबके एकमात्र स्वामी भगवान्‌ श्रीकृष्ण हैं, बार-बार किया गया है। देवताओ! मैं जिसके जो भक्तोंपर अनुग्रह करनेके लिये दिव्य विग्रह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.1060)
- **Original**: वंशमें उत्पन्न ःूँ और जिसका बालक-शिष्य हूँ, धारण करते हैं। जिसे सभी पाना चाहते हैं, वह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.1061)
- **Original**: उन्हींका यह ज्ञानमय वचन है। तुम लोग इसे सत्यलोक या नित्य बैकुण्ठधाम समस्त ब्रह्माण्डसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.1062)
- **Original**: सुनो और समझो। देवेश्वर सुरेश! गन्धर्वको शीघ्र ऊपर है। उससे भी ऊपर गोलोक है, जिसका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.1063)
- **Original**: जीवित करो। विचार व्यक्त करनेपर स्वतः ज्ञात विस्तार पचास करोड़ योजन है। वैकुण्ठधाममें हो जाता है कि कौन मूर्ख है और कौन विद्वान? वे सनातन श्रीहरि चार भुजाधारी लक्ष्मीपतिके अत: यहाँ वाग्युद्धका क्‍या प्रयोजन है? रूपमें निवास करते हैं। वहाँ सुनन्द, नन्द और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.1064)
- **Original**: . शौनक! ऐसा कहकर बे ब्राह्मणरूपधारी कुमुद आदि पार्षद उन्हें थेरे रहते हैं। गोलोकमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.1065)
- **Original**: भगवान्‌ विष्णु चुप हो गये और जोर-जोरसे हँसने वे सनातनदेव दो भुजाओंसे युक्त राधावल्लभ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.1066)
- **Original**: लगे। (अध्याय 17) जज जल]
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.1067)
- **Original**: * संक्षिप्त ग्रह्मवैवर्तपुराण * #%ऋ%%$%$%$%कऊ%%%%$%%%%%%%#%%#########%#/% 84% %#%
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.1068)
- **Original**: : %ऋऋकऋकऋऊऋश कक कक कऋऋऋकऋकऋऊश्कककक कक 64.0 $ 5
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.1069)
- **Original**: 8 848 4. 0 8 280 0 2 6 2 6 66464) 1।6185 8 ।28]8261682!88[
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.1070)
- **Original**: ब्रह्मा आदि देवताओंद्वारा उपबहणको जीवित करनेकी चेष्टा, मालावतीद्वारा भगवान्‌ श्रीकृष्णका स्तवन, शक्तिसहित भगवान्‌का गन्धर्वके शरीरमें प्रवेश तथा गन्धर्वका जी उठना, मालावतीद्वारा दान एवं मड़ूलाचार तथा पूर्वोक्त स्तोत्रके पाठकी महिमा सौति कहते हैं-- भगवान्‌ विष्णुकी मायासे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.1071)
- **Original**: हैं; पालक विष्णु और साक्षात्‌ जगत्संहारक शिव मोहित हुए ब्रह्मा और शिव आदि देवता ब्राह्मणके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.1072)
- **Original**: भी जिनकी सेवामें निरन्तर तत्पर रहते हैं; सब साथ मालावतीके निकट गये। ब्रह्माजीने शवके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.1073)
- **Original**: देवता, मुनि, मनु, सिद्ध, योगी और संत-महात्मा शरीरपर कमण्डलुका जल छिड़क दिया और
- **Translation**: 

---

