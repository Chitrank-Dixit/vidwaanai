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

### Verse 1 (Vaivtpuran 543.16394)
- **Original**: अपने गृहको प्रस्थित हुईं। इधर वसुदेव और लिये भी दुर्लभ है। वे आनन्दपूर्वक वह सारा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16395)
- **Original**: देवकोने पुत्रके कल्याणके लिये अनेक प्रकारके रहस्य तुम्हें बतलायेंगे। इतना कहकर जगदीश्वर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16396)
- **Original**: रतन, मणि, वस्त्र, सोना, चाँदी, मोतियों और श्रीकृष्ण वसुदेवजीकी सभामें चले गये और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16397)
- **Original**: हीरोंके हार और अमृत-तुल्य मिष्टान्न भट्ट ब्राह्मणोंको क्षणभर वहाँ ठहरकर पिताकी आज्ञासे महर्षि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16398)
- **Original**: आदरपूर्वक हर्षपूर्ण मनसे समर्पित किये। फिर सांदीपनिके आश्रमको प्रस्थित हुए। यलपूर्वक महोत्सव मनाया गया; जिसमें वेद- तदनन्तर यशोदासहित नन्दजी विनयपूर्वक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16399)
- **Original**: पाठ, हरिनाम-संकीर्तन और ब्राह्मणोंकों भोजन वसुदेव-देवकीसे वार्तालाप करके दुःखी हृदयसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16400)
- **Original**: कराया गया। इसके बाद जाति-भाइयोंकों यथोचित जानेको उद्यत हुए। उस समय देवकीने नन्दजीको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16401)
- **Original**: रूपसे मनोहर मणि, माणिक्य, मोती और वस्त्र मुक्तामणि, सुवर्ण, माणिक्य, होरा, रत्न और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16402)
- **Original**: पुरस्काररूपमें दिये। अग्निशुद्ध वस्त्र भेंट किये। वसुदेवजी और (अध्याय 100-101) #3+# कर पि20/5000 50 बलरामसहित श्रीकृष्णका विद्या पढ़नेके लिये महर्षि सांदीपनिके निकट जाना, गुरु और गुरुपल्रीद्वारा उनका स्वागत और विद्याध्ययनके पश्चात्‌ गुरुदक्षिणारूपमें गुरुक मृतक पुत्रको उन्हें वापस देकर घर लौटना श्रीनारायण कहते हैं--नारद! श्रीकृष्णने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16403)
- **Original**: विद्याध्ययन कराइये। तब ' 34--बहुत अच्छा '--यों बलरामके साथ हर्षपूर्वक सांदीपनिके गृह जाकर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16404)
- **Original**: कहकर मुनिवर सांदीपनिने हर्षपूर्वक मधुपर्कप्राशन, अपने उन गुरुदेव तथा पतिब्नरता गुरुपत्नीको
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16405)
- **Original**: गौ, वस्त्र और चन्दनट्वारा उनका आदर-सत्कार नमस्कार किया और उन्हें भेंटरूपमें रत्न एवं मणि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16406)
- **Original**: किया, मिष्टान्न भोजन कराया, सुबासित पानका समर्पित की। तत्पश्चात्‌ उनसे शुभाशीर्वाद लेकर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16407)
- **Original**: बीड़ा दिया, मधुर वार्तालाप किया और उन वे श्रीहरि उन गुरुदेवसे यथोचित वचन बोले।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16408)
- **Original**: परमेश्वरका स्तवन करते हुए कहा। श्रीकृष्णने कहा--विप्रवर! आपसे अपनी सांदीपनि बोले--भक्तोंके प्राणवल्लभ ! तुम अभीष्ट विद्या प्राप्त करूँगा-ऐसी मेरी लालसा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16409)
- **Original**: परब्रह्म, परमधाम, परमेश्वर, परात्पर, स्वेच्छामय, है; अत: शुभ मुहूर्त निश्चय करके मुझे यथोचितरूपसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16410)
- **Original**: स्वयंज्योति, निर्लिप्त, अद्वितीय, निरड्डश, भक्तोंके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16411)
- **Original**: *अ्रीकृष्णजन्मखण्ड ] 719 #%#कऋकऋऋककऋ्क््ऋ ऋ्््ऋ ऋ ऋ्क्ऋ्ऋछ $%%%$%%ऋक %ऋऋऊऋफ कक 6644 ##### #########%%%% एकमात्र स्वामी, भक्तोंके इष्टदेव, भक्तानुग्रहमूर्ति
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16412)
- **Original**: सफल हो गया। मैंने जिस हाथसे तुम्हें इच्छित और भक्तोंका मनोरथ पूर्ण करनेके लिये कल्पतरु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16413)
- **Original**: अन्न प्रदान किया है, वह मेरा दाहिना हाथ सफल हो। ब्रह्मा, शिव और शेष तुम्हारी वन्दना करते
- **Translation**: 

---

