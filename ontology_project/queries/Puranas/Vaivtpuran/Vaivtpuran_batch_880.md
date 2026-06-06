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

### Verse 1 (Vaivtpuran 543.15914)
- **Original**: आविरभूव. सा दुर्गा सूर्यकोटिसमप्रभा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15915)
- **Original**: नाराणणेन कृपया प्रेरिता परमात्मता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15916)
- **Original**: शिवस्य पुरत: शीघ्र॑ शिवाय च जयाय च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15917)
- **Original**: इत्युवाच महादेवी मायाशक्‍्त्यासुर॑ जहि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15918)
- **Original**: (88। 15-38)
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15919)
- **Original**: + श्रीकृष्णजन्मखण्ड * 693 5#4##5%# 55% 55% % 5 # 5 # 545 # % # 5 ऊ 4 ऊक ऊद्र कक डक ऊड ड अड ऊ 55 कद कद अंक क 54 55% 5 45% 84 8886 8 5, विप्रेन्द्र ! श्रीकृष्णका वचन सुनकर नन्दने इस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15920)
- **Original**: गोपिकागण, बालसमूह और विशेषतया राधा--ये स्तोत्रद्वारा सम्पूर्ण सम्पत्तियोंको प्रदान करनेवाली सभी एकत्र स्थित हैं। उन बन्धुवर्गोंक साथ पार्वतीका स्तवन किया। मुने! तब दुर्गाने उन्हें कर्मानुसार यहीं सुख भोगकर उत्तम गोलोककों गोलोक-वासरूप अभीष्ट वर प्रदान किया। साथ जाओ। तात! यशोदा, रोहिणी, गोपिकागण, ही जो वेदमें भी नहीं सुना गया है, वह परम गोपबालक, वृषभानु, गोपसमूह, राधाकी माता दुर्लभ ज्ञान, गोकुलकी राजाधिराजता और परम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15921)
- **Original**: कलावती और राधाके साथ आप पर्थिव देहको दुर्लभ श्रीकृष्ण-भक्ति भी दो। इसके अतिरिक्त त्यागकर और दिव्य देह धारण करके गोलोक नन्दको श्रीकृष्णकी दासता, महत्ता और सिद्धता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15922)
- **Original**: जायँगे। राधा और राधाकी माता कलावतीकी भी प्राप्त हुई। इस प्रकार वरदान देकर और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15923)
- **Original**: उत्पत्ति योनिसे नहीं हुई है; अतः बह निश्चय शम्भुके साथ वार्तालाप करके दुर्गाजी अदृश्य हो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15924)
- **Original**: ही अपने उसी नित्वदेहसे गोलोकमें जायगी। गयीं। तब देवता और मुनिगण भी नन्दनन्दनकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15925)
- **Original**: कलावती पितरोंकी मानसी कन्या है; अतः धन्य स्तुति करके अपने-अपने स्थानको चले गये।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15926)
- **Original**: और माननीय है। इसी प्रकार सीतामाता, तत्पश्चात्‌ श्रीकृष्णने नन्दसे कहा--'नन्दजी! [
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15927)
- **Original**: दुर्गामाता, मेनका, दुर्गा, तारा और सुन्दरी अब आप दुर्लभ ज्ञानसे संयुक्त होनेके कारण सीता-ये सभी अयोनिजा तथा धन्य हैं। वे तथा मोहका त्याग करके प्रसन्नमनसे न्रजवासियोंसहित
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15928)
- **Original**: मेना और कलावती योनिसे न उत्पन्न होनेके ब्रजको लौट जाइये। व्रजराज ! जाइये, जाइये, घर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15929)
- **Original**: कारण धन्यवादको पात्र हैं। तात! इस प्रकार मैंने जाइये, ब्रजको पधारिये। अब आपको सम्पूर्ण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15930)
- **Original**: परम दुर्लभ गोपनीय आख्यानका बर्णन कर दिया तत्त्वोंका ज्ञान हो गया। आपने मुनियों तथा तथा मैंने और दुर्गने आपको यह वरदान भी देवताओंके दर्शन कर लिये और मेरेद्वारा अत्यन्त
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15931)
- **Original**: दे दिया।' श्रीकृष्णका वचन सुनकर श्रीकृष्णभक्त दुर्लभ नाना प्रकारके इतिहास, धनवर्धक आख्यान
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15932)
- **Original**: ब्रजेश्वर उन भक्तवत्सल जगदीश्वरसे पुनः बोले। और जन्म एवं पापका विनाश करनेवाला दुर्गकका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15933)
- **Original**: । नन्दने कहा--प्रभो! श्रीकृष्ण! चारों युगोंके स्तोत्रराज भी सुन लिया। जो कुछ सामने
- **Translation**: 

---

