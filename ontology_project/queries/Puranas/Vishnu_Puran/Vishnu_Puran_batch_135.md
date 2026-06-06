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

### Verse 1 (Vishnu Puran 0.2681)
- **Original**: 14 बद्‌ सुताः सुपहासस्त्वास्ताग्रायाः परिकीत्तिता: । झुकी इयेनी च भासी च सुग्रीवीशुचिगृदध्रिकाः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2682)
- **Original**: 15 श्रीपराहारजी खोल्ले--संह्लादके पुत्र आयुष्मान्‌ जित्रि और बाष्कल थे तथा प्रद्टादके पुत्र विशेचन थे और विरोचनसे बलिका जञ्म हुआ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2683)
- **Original**: हे महामुने ! बलिके सौ पूत्र थे जिनमें बाणासुर सबसे बड़ा था। रिरिण्याक्षके पुत्र उत्कुर, झकुनि, भूतसन्तापन, महानाभ, महानाहु तथा कालनाभ आदि सभी महाबलबान्‌ थे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2684)
- **Original**: (कश्यपजीकी एक दूसरी स्त्री) दनुके पुत्र द्विमूर्धा, शम्बर, अयोमुस्तल, शेकुशिश, कपिल, शंकर, एककऋ, महाबाहु, तारक, महाबल, स्वर्भानु, वृषपर्ता, महानली पुल्लेम और परमपग्क्रमी विप्रचिति थे । ये सब दनुके पुत्र विख्यात हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2685)
- **Original**: स्वर्भानुकी कन्या प्रभा थी तथा हार्मिष्ठा, उपदानी और हयद्िरा--ये वृषपर्बाकी परम सुन्दरी कन्याएँ लिख्यात हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2686)
- **Original**: वैश्वानर्की पुल्लेमा और काल्का दो पुत्रियाँ थीं। हे महाभाग ! जे दोनों कन्याएँ. म्ररीचितन्‍्दन कठयपजीवी भार्या हुईं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2687)
- **Original**: उनके पुत्र स्राठ हजार दानव- श्रेष्ठ हुए। मरीचिनन्दन कश्यपजीके वे सभी पुत्र पौलोम और काल्केय कहल्ाये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2688)
- **Original**: इनके सिवा विप्रचित्तिके सिंहिकाके गर्भसे और भी बहुत से महाबलवान्‌, भयंकर और अतिक्रूर पुत्र उत्पन्न हुए
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2689)
- **Original**: वे व्यंश, शल्य, बलवान्‌ नभ, महाबल्ती वातापी, नम्मुचि, इल्नल, खसूम, अन्धक, नरक, कालनाभ, महायीर, स्वर्भानु और महादैत्य वक्‍्त्र योधी थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2690)
- **Original**: ये सब दानवश्रेष्ठ दनुके लंशको बढ़ानेवाले थे। इनके और भी सैकड़ों-हजारों पुत्र-पौज्ादि हुए
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2691)
- **Original**: महान्‌ तपस्थाद्वारा आत्मज्ञानसम्पन्न दैत्यबर प्रद्वादजीके कुछमें निवातकवच नामक दैस्य उत्पन्न हुए
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2692)
- **Original**: कश्यपजौकी स्त्री तामप्राकी झुकी, झ्येनी, भासी, सुग्रीवी, भुधि और गृदघ्चिका--ये छः अति प्रभाव- शालिनी कन्याएँ कही जाती हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2693)
- **Original**: 97 शुकी शुकानजनबदुलूकप्रत्युलूकिकान्‌ । इयेनी इ्येनॉस्तथा भासी भासान्गुद्ध्नाँश्व गृद्क़ापि
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2694)
- **Original**: 16 अआुच्यौदकान्पक्षिगणान्सुप्रीवी तु व्यजायत । अश्वानुष्टान्गर्दभांश्व ताप्राबंश: प्रकीरत्तित:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2695)
- **Original**: 17 बिनतायास्तु द्रौ पुत्री विख्यातो गरुढारुणौ । सुपर्ण: पततां श्रेष्ठो दारुण: पन्नगाशनः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2696)
- **Original**: 18 सुरसायां सहस्न॑ तु सर्पाणाममितोजसाम्‌। अनेकशिरसां ब्रह्मन्‌ खेच्नराणां महात्मनाम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2697)
- **Original**: 19 काद्रवेयास्तु बलिनः सहस्रममितौजस: । सुपर्णवशगा ब्रह्मन्‌ जन्ञषिरे नैकमस्तकाः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2698)
- **Original**: 20 तेषां प्रधानभूतास्तु शेषवासुकितक्षकाः । शद्धश्वेतो महापद्मः कम्बल्ाश्चतरौ तथा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2699)
- **Original**: 21 नाग: ककॉंटकथनज्ञयो । एते चान्‍्ये च बहवो दन्‍्दशूका विघोल्बणा:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2700)
- **Original**: 22 गण क्रोधव्श विद्धि तस्या: सबें च दंष्टिण: । स्थलजा: पक्षिणो5ब्जाअ्न दारुणा: पिशिताशना:
- **Translation**: 

---

