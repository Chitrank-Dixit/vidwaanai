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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.41)
- **Original**: सुमुखश्वैकदन्तश्च कपिलो गजकर्णकः । लम्बोदरश्च विकटो... विस्‍्ननाशो. विनायक:
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.42)
- **Original**: घूम्रकेतुर्गणाध्यक्षो भालचन्द्रो गजाननः
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.43)
- **Original**: द्वादशैतानि . नामानि... यः.. पठेच्छुणुयादपि
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.44)
- **Original**: विद्यारम्मे विवाहे च.. प्रवेशे निर्गमे तथा। संग्रामे संकटे चैव विषघ्नत्तस्य न. जायते
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.45)
- **Original**: शुक्लाम्बरधरं ... देव॑ शशिवर्ण.. चतुर्भजमू। _प्रसन्नवदनं.. ध्यायेत्‌ सर्वविष्नोपशान्तये
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.46)
- **Original**: अभीप्सितार्थसिद्धयर्थ पूजितो यः. सुराद्सुरैः । सर्वविष्नहरस्तस्मै गणाधिपतये नमः
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.47)
- **Original**: सर्वमंगलमां गल्ये शिवे ! सवर्थिसाधिके । शरण्ये च्यम्बके गौरि नारायणि ! नमोइस्तुते
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.48)
- **Original**: तदेव लग्न॑सुदिन॑तदेव, ताराबलं चन्द्रबल तदेव। विद्याबलं दैवबल॑ तदेव, लक्ष्मीपते ! तेडडूप्नियुगं स्मरामि
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.49)
- **Original**: लाभस्तेषां.... जयस्तेषां.... कुतस्तेषां. पराजयः। येषामिन्दीवरश्यामो हृदयस्थो... जनार्दन:
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.50)
- **Original**: सर्वेष्वारम्मकार्येषु नयखिभुवनेश्वरा: । देवा दिशन्तु नः. सिद्धि. ब्रहोशानजनार्दना:
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.51)
- **Original**: इसके बाद कुशाक्षत जल-द्रव्य॑ के साथ पुष्प और सुपाड़ी लेकर संकल्प करे। 0 श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.52)
- **Original**: अथ संकल्प ऊँ विष्णुर्विष्णुर्विष्णु: । ऊँ? तत्सदय श्रीमद्गगवतो गहापुरुषस्य विष्णो राज्ञया प्रवर्तमानस्य श्रीब्रह्मणोडद्दि . दितीयपरादू्धें. श्रीश्वेतवाराहकल्पे वैवस्वतमन्वन्त- - रे5ष्टारविशतितमे कलियुगे कलिप्रथमचरणे जम्बूदीपे भरतखण्डे आयर्विर्तैक देशान्तरगते श्रीमदिष्णु प्रजापति क्षेत्रे (यथा प्रयाग क्षेत्र) अमुकसंवत्सरे अमुक अयने अमुक कऋतौ अमुक मासे अमुक पक्षे अमुक तिथौ अमुक वासरे अमुक नक्षते अमुकत योगे अमुक करणे, अमुक राशिस्थिते सूर्यें, चन्द्रे यथा- स्थानस्थितेषु सत्सु ग्रहेषु एवं गुणविशिष्टायां वेलायां (लग्ने वा), अमुकगोज्रोत्पन्नः (शर्मा-वर्मा, गुप्तदासोउहम) सपत्नीकोउहं थुतिस्मृतिपुराणोक्तफलप्राप्तये (अमुककार्य-सिद्ध्र्थ) यथोक्तविधानेनात्र संस्थापित-कलशो परि श्रीदिश्वकर्मा- पूजनमहं करिष्ये । तन्नादौ निर्विष्नकृत्यसम्पादनार्थ श्रीगणेशाम्बिकयो: पूजन कलशस्थापनं नवय्रहदीनां पूजन करिष्ये । तन्नादौ तण्डुलपूर्णपात्रे5ष्टदलं निर्माय पूंगीफलमयं गणेशं, गोमयीं गौरीश्व संस्थाप्य प्लोपचारैः पूजयेत्‌ । प्ललोकपालानू नवग्रह्मदीश्द पूजयित्वा घोडशमातृणां पूजन कुर्यात्‌ । तचथा-- संकल्प के बाद चावल से भरे पात्र में रोली से अप्टदल बनाकर सुपाड़ी का गणेश तथा गोमय की गौरी की पूजा पंचोपचार अथवा पोडशोपचार विधि से करनी चाहिए। साथ ही पश्न-लोकपाल एवं नवग्रह की पूजा करके षोडशमातृका पूजन भी केरे। जैसे- अथ गणेशपूजनम्‌ एहोहि हेरम्ब ! महेशपुत्र समस्तविध्नौघविनाशदक्ष । मांगल्यपूजा-प्रथमं प्रधान ! गृहाण पूजां भगवन्‌ नमस्ते
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.53)
- **Original**: आगच्छ भगवन्‌ देव स्वस्थानातरमेश्वर ! ऊहं पूजां करिष्यामि सदा त्व॑ सम्मुखो भव
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.54)
- **Original**: इस मंत्र से गणेशजी का आवाहन करके नीचे के मंत्र से प्रतिष्ठा करे- एघषु चाक्षत-पुज्जेषु पूंगीफल-सुमूर्तिषु । पूजार्थ वै प्रतिष्ठामि सुप्रतिष्ठ सुरेश्वर !
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.55)
- **Original**: इसके बाद गणानां त्वा गणपति...इस वेदमंत्र को उच्चारण करके संक्षेप में इस प्रकार पूजन करे-- एतत्‌ पाद्य॑ गणपतये नमः, एघोडर्घों गणपतये नमः । एतत्स्नानीयं जलं गणपतये नमः, इसमे वख्यज्ञोपवीते गणपतरे नमः । इदं गन्ध गणपतये नमः, इमे अक्षता: गणपतये नमः । “ऊँ घूरसि घूर्व घूर्वन्तं योउस्मानू धूर्वती” इति मंत्रेण धघूप॑ गणपत्तये नमः । “अग्निरज्यों ति* इति मंत्रेण दीपं॑ दर्शयामि । हस्तप्रक्षालनमू । गणपतये नमः । नैवेच॑ निवेदयामि गणपतये नमः, नैवेद्यान्ते आचमनीयं समर्पयामि । गणपतये नमः । ताम्बूलं सम. गणपतये नमः । फल दक्षिणां च सम. गणपतये श्री विश्वकर्मा पुराण एवं पूजन पद्धति 17
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.56)
- **Original**: के... “ऊ- कदर... नमः ! अन्ते पुष्याज्ज्लिं दघात्‌-- प्मालती-मल्लिकाजाती-शत्तपन्नादिसं युतम्‌ । पुष्पाज्जलि गुहाणेश ! तव पादयुगार्पितमू
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.57)
- **Original**: प्रार्थना-- विघ्नेश्वराय वरदाय सुरप्रियाय लम्बोदराय सकलाय जगदिताय
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.58)
- **Original**: नागाननाय सुरयज्ञविभूषिताय गौरीसुताय गणनाथ ! नमो नमस्ते
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.59)
- **Original**: अनेन पूजनेन श्रीगणेश: प्रीयतामू । अथ गौरीपूजनम्‌ नीचे लिखे हुए वैदिक तथा तांत्रिक मंत्रों दारा 'गोमयी' गौरी देवी का आवाहन एवं पूजन करना 'चाहिए। ं ऊँ श्रीश्च ते लक्ष्मीशव पल्याबहो रात्रे पशश्वें नक्षत्राणि रूपमशिवनौ व्यात्तमू । इष्णन्‌ निषाणामुम्म 5इषाण सर्वलोक॑ म5इघाण
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.60)
- **Original**: सर्वमंगलमंगल्ये... शिवे.. सवर्थिसाधिके ! शरण्ये त्यम्बके गौरि नारायणि ! नमोस्तुते
- **Translation**: 

---

