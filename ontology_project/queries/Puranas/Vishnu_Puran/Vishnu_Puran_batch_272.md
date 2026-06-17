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

### Verse 1 (Vishnu Puran 0.5421)
- **Original**: सम्पूर्ण प्राणी, यह अन्न और पैं---सभी विष्णु हैं; क्योकि उनसे भिन्न और कुछ है ही नहीं। अतः मैं समस्त धूतोंका दारीर्रूप यह अतन्र उनके पोषणके लिये दान करता हूँ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5422)
- **Original**: यह जो चौदह प्रकारका * भूतसमुदाय है उसमें जितने भी प्राणिगण अवस्थित हैं उन सबकी तृप्तिक लिये मैंने यह अन्न प्रस्तुत किया है; वे इससे प्रसत्र हों'
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5423)
- **Original**: इस प्रकार उच्चारण करके गृहस्थ पुरुष श्रद्धापूर्तक समस्त जीवोकि उपकारके र्थ्ये पृथिबीमें अन्नदान करे, क्योंकि गृहस्थ ही सबका आश्रय है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5424)
- **Original**: हे नरेध्वर ! तदनन्तर कुत्ता, चाप्डाल, पश्चिगण तथा और भी जो कोई पतित एवं पुत्रहोन पुरुष हों उनको तृप्तिके छिये पृथिजरीमें बलिभाग रखे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5425)
- **Original**: फिर गो-दोहनकालपर्यन्त अथवा इच्छानुसार इससे भी कुछ अधिक देर अतिथि अहण करनेके लिये घरके * चौदह भूतसमुदायोक्त्र वर्णन इस प्रकार किया गया है-- 'अष्टविध देलत्व॑ तैर्यग्योन्यश पञ्ञधा भवति। मानुर्ष्य चैकनिध समासतो भौतिकः सर्ग:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5426)
- **Original**: अधांत्‌ आठ प्रकारका देवसम्बन्धी, पाँच प्रकाज़्का तिर्यम्योगिसम्बधी और एक प्रकारका मनुष्ययोनिसम्बधी--यह संक्षेपसे भौतिक सर्ग कहलाता है। इनका पृथक्‌ पृथक्‌ विवरण इस प्रकार है--- सिद्धगुद्मयकगशख्र्वयक्षराक्षसपत्नगा: । विद्याघरा: पिद्ाचाश्व निर्टिश देवयोनयः #
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5427)
- **Original**: आ 11 ] अति्थि तत्र सम्प्राप्तं पूजयेत्स्वागतादिना । तथासनप्रदानेन पादप्रक्षालनेन च
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5428)
- **Original**: 59 श्रद्धया चान्नदानेन प्रियप्रश्नोत्तेण च। गछ्छतश्चानुयानेन प्रीतिमुत्पादयेद्‌ गृही
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5429)
- **Original**: 60 अज्ञातकुलनामानमन्यदेशादुपागतम्‌ । पूजयेदतिथिं सम्यद्ध नैकग्रामनिवासिनम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5430)
- **Original**: 61 अकिझ्ननमसम्बन्धमज्ञातकुलशीलिनम्‌ _। असप््पूज्यातिथिं भुक्त्वा भोक्तुकामं व्रजत्यधः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5431)
- **Original**: 62 स्वाध्यायगोत्राचरणमपृष्ठा च तथा कुलछम्‌। हिरण्यगर्भवुद्धया ते मन्येताभ्यागतं गृही
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5432)
- **Original**: 63 पित्र्थ चापरं विप्रमेकमप्याशयेन्रुप । तदेश्यं विदिताचारसम्भूति पाक्रयज्ञिकम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5433)
- **Original**: 64 अन्नाग्रश्न समुदधृत्य हन्तकारोपकल्पितम्‌ । निर्वापभूत भूपाल श्रोश्रियायोपपादयेत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5434)
- **Original**: 65 दत्त्वाचभिक्षात्रितयं परिव्राडब्रह्माचारिणाम्‌ । इच्छया च बुधो द्धद्याद्विभवे सत्यवारितम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5435)
- **Original**: 66 इत्येतेडतिथय: प्रोक्ता: प्रागुक्ता भिक्षवश्ष ये । चतुरः पूजयित्वैतान्रणप पापाठ्मुच्यते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5436)
- **Original**: 67 अतिथिय॑स्थ भप्माशों गृहात्मतिनिवर्तते । स तस्मे दुष्कृत दत्त्वा पुण्यमादाय गच्छति
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5437)
- **Original**: 68 धाता प्रजापति: शक्रो बहिर्सुगणो3र्यमा । प्रविज्यातिथिमेते वे चुझन्तेत्न नरेश्वर
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5438)
- **Original**: 69 तस्मादतिथिपूजायां यतेत सतत॑ नर:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5439)
- **Original**: सकेवलमर्घ भुझ्ते यो भुदन्ते हतिथि विना
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5440)
- **Original**: 70 ततः स्ववासिनीदुःखिगर्भिणीवृद्धबालकान्‌ । भोजयेस्संस्कृतान्नेन प्रथम॑ चरम॑ गृही
- **Translation**: 

---

